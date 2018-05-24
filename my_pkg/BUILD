python_binary(
    name='my_pkg',
    source='foo.py',
    dependencies=[
        ':foobar',
        ':requests',
        ':shapely',
    ],
    platforms=[
        'linux-x86_64-cp-27-mu',
        'macosx-10.13-x86_64',
    ],
    zip_safe=False,
)

python_library(
    name='foobar',
    sources=rglobs('*.py'),
)

python_requirements()
