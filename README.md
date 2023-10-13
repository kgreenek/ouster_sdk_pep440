# ouster_sdk_pep440
Minimal repo to demonstrate https://github.com/ouster-lidar/ouster_example/issues/560

Tested on Ubuntu 22.04.

### How to run

Install bazelisk:

```bash
cd ~/Downloads
mkdir -p ~/bin
wget https://github.com/bazelbuild/bazelisk/releases/download/v1.17.0/bazelisk-linux-amd64
chmod 755 bazelisk-linux-amd64
mv bazelisk-linux-amd64 ~/bin/bazel
export PATH="$HOME/bin${PATH:+":$PATH"}"
```

Now when you invoke `bazel` it will be using bazelisk.

Run the example:

```bash
bazel run //ouster_pcap_record
```

You should see an error similar to the following:

```
ERROR: /home/kevin/src/kgreenek/ouster_sdk_pep440/ouster_pcap_record/BUILD.bazel:4:10: //ouster_pcap_record:ouster_pcap_record depends on @pip_deps_ouster_sdk//:pkg in repository @pip_deps_ouster_sdk which failed to fetch. no such package '@pip_deps_ouster_sdk//': whl_library pip_deps_ouster_sdk failed: Collecting ouster-sdk==0.9.0 (from -r /tmp/tmp7wuogsxy (line 1))
  Using cached ouster_sdk-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (4.3 MB)
Saved ./ouster_sdk-0.9.0-cp310-cp310-manylinux_2_17_x86_64.manylinux2014_x86_64.whl
 (Traceback (most recent call last):
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/python_3_10_6_x86_64-unknown-linux-gnu/lib/python3.10/runpy.py", line 196, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/python_3_10_6_x86_64-unknown-linux-gnu/lib/python3.10/runpy.py", line 86, in _run_code
    exec(code, run_globals)
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/rules_python/python/pip_install/tools/wheel_installer/wheel_installer.py", line 200, in <module>
    main()
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/rules_python/python/pip_install/tools/wheel_installer/wheel_installer.py", line 192, in main
    _extract_wheel(
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/rules_python/python/pip_install/tools/wheel_installer/wheel_installer.py", line 132, in _extract_wheel
    whl_deps = sorted(whl.dependencies(extras_requested) - self_edge_dep)
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/rules_python/python/pip_install/tools/wheel_installer/wheel.py", line 79, in dependencies
    if req.marker is None or any(
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/rules_python/python/pip_install/tools/wheel_installer/wheel.py", line 80, in <genexpr>
    req.marker.evaluate({"extra": extra})
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/pypi__setuptools/pkg_resources/_vendor/packaging/markers.py", line 252, in evaluate
    return _evaluate_markers(self._markers, current_environment)
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/pypi__setuptools/pkg_resources/_vendor/packaging/markers.py", line 158, in _evaluate_markers
    groups[-1].append(_eval_op(lhs_value, op, rhs_value))
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/pypi__setuptools/pkg_resources/_vendor/packaging/markers.py", line 116, in _eval_op
    return spec.contains(lhs, prereleases=True)
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/pypi__setuptools/pkg_resources/_vendor/packaging/specifiers.py", line 568, in contains
    normalized_item = _coerce_version(item)
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/pypi__setuptools/pkg_resources/_vendor/packaging/specifiers.py", line 36, in _coerce_version
    version = Version(version)
  File "/home/kevin/.cache/bazel/_bazel_kevin/0bfc23b9cb417e948c9bb9daad8abbda/external/pypi__setuptools/pkg_resources/_vendor/packaging/version.py", line 198, in __init__
    raise InvalidVersion(f"Invalid version: '{version}'")
pkg_resources.extern.packaging.version.InvalidVersion: Invalid version: '#34~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Sep  7 13:12:03 UTC 2'
) error code: '1'
```

If you change rules_python to version 0.25.0 instead of 0.26.0, the example runs successfully.
