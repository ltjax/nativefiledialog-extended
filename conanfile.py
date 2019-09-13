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
        if self.settings.os == "Linux":
            self._add_libraries_from_pc("gtk+-3.0")
        elif self.settings.os == "Macos":
            frameworks = ["AppKit"]
            for framework in frameworks:
                self.cpp_info.exelinkflags.append("-framework {0}".format(framework))
                self.cpp_info.sharedlinkflags.append("-framework {0}".format(framework))

    def _add_libraries_from_pc(self, library):
        pkg_config = tools.PkgConfig(library)
        libs = [lib[2:] for lib in pkg_config.libs_only_l]  # cut -l prefix
        lib_paths = [lib[2:] for lib in pkg_config.libs_only_L]  # cut -L prefix
        self.cpp_info.libs.extend(libs)
        self.cpp_info.libdirs.extend(lib_paths)
        self.cpp_info.sharedlinkflags.extend(pkg_config.libs_only_other)
        self.cpp_info.exelinkflags.extend(pkg_config.libs_only_other)