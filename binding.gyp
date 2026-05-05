{
  "targets": [{
    "target_name": "udev",
    "cflags!": [ "-fno-exceptions" ],
    "cflags_cc!": [ "-fno-exceptions" ],
    "xcode_settings": { "GCC_ENABLE_CPP_EXCEPTIONS": "YES",
      "CLANG_CXX_LIBRARY": "libc++",
      "MACOSX_DEPLOYMENT_TARGET": "10.7",
    },
    "msvs_settings": {
      "VCCLCompilerTool": { "ExceptionHandling": 1 },
    },
    "sources": [ "main.cc", "udev.cc" ],
    "libraries": [
      "<!(pkg-config --libs libudev)"
    ],
    "include_dirs" : [
      "<!@(node -p \"require('node-addon-api').include\")",
      "<!(pkg-config --cflags libudev)"
    ],
    'dependencies': [
      "<!(node -p \"require('node-addon-api').gyp\")"
    ]
  }]
}
