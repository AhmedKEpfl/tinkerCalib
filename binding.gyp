{
    "targets": [{
    	"target_name": "tinkercalib",
    	"sources": ["src/tinkerCalib.cc", "src/calibration.cpp", "src/posConverter.cpp"],
        "include_dirs": [
            '/usr/local/include'
        ],
        "cflags!": ["-fno-rtti", "-fno-exceptions"],
        "cflags_cc!": ["-fno-rtti", "-fno-exceptions"],
    	"libraries": [
            '<!@(pkg-config --libs opencv)'
    	]
    }],
}
