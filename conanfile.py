from conans import ConanFile, CMake, tools


class NativeFileDialogExtendedConan(ConanFile):
    name = "nativefiledialog-extended"
    version = "1.0"
    license = "zlib"
    author = "Marius Elvert marius.elvert@googlemail.com"
    url = "https://github.com/ltjax/nativefiledialog-extended"
    description = "Small C and C++ libraries that portably invoke native file open, folder select and save dialogs."
    topics = ("file-dialog",)
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared":False}
    generators = "cmake"
    exports_sources = "src/*", "test/*", "CMakeLists.txt"

    def _configured_cmake(self):
        cmake = CMake(self)
        cmake.configure(source_folder=".", defs={})
        return cmake

    def build(self):
        self._configured_cmake().build()

    def package(self):
        self._configured_cmake().install()

    def package_info(self):
        self.cpp_info.libs = ["nfd"]
