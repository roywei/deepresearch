from backend.orchestrator import compile_results


def test_compile_results():
    summary = compile_results([('Title', 'https://example.com')])
    assert 'Title' in summary
    assert 'https://example.com' in summary
