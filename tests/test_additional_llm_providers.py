import sys
import types
from unittest.mock import MagicMock, patch

import agents


def _fake_openai_module(reply="provider response"):
    module = types.ModuleType("openai")
    sdk_client = MagicMock()
    sdk_client.chat.completions.create.return_value = types.SimpleNamespace(
        choices=[types.SimpleNamespace(message=types.SimpleNamespace(content=reply))]
    )
    module.OpenAI = MagicMock(return_value=sdk_client)
    return module, sdk_client


def test_deepseek_uses_official_openai_compatible_endpoint_and_current_default():
    fake_openai, sdk_client = _fake_openai_module()
    with patch.dict(sys.modules, {"openai": fake_openai}), \
         patch.dict("os.environ", {}, clear=False):
        client = agents.create_llm_client("deepseek", "sk-deepseek", "")
        result = client.complete("system", [{"role": "user", "content": "hello"}])

    fake_openai.OpenAI.assert_called_once_with(
        api_key="sk-deepseek",
        base_url="https://api.deepseek.com",
    )
    assert sdk_client.chat.completions.create.call_args.kwargs["model"] == "deepseek-v4-flash"
    assert result == "provider response"


def test_qwen_uses_dashscope_endpoint_and_supports_region_override():
    fake_openai, sdk_client = _fake_openai_module()
    singapore_url = "https://dashscope-intl.aliyuncs.com/compatible-mode/v1"
    with patch.dict(sys.modules, {"openai": fake_openai}), \
         patch.dict("os.environ", {"QWEN_BASE_URL": singapore_url}):
        client = agents.create_llm_client("qwen", "sk-qwen", "")
        client.complete("system", [{"role": "user", "content": "hello"}])

    fake_openai.OpenAI.assert_called_once_with(api_key="sk-qwen", base_url=singapore_url)
    assert sdk_client.chat.completions.create.call_args.kwargs["model"] == "qwen3.7-plus"


def test_provider_key_validation_and_registry():
    assert {"deepseek", "qwen"}.issubset(agents.VALID_PROVIDERS)
    assert agents.validate_api_key_for_provider("deepseek", "bad-key")
    assert agents.validate_api_key_for_provider("qwen", "bad-key")
    assert agents.validate_api_key_for_provider("deepseek", "sk-valid") == ""
    assert agents.validate_api_key_for_provider("qwen", "sk-valid") == ""
