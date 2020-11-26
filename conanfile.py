from conans import ConanFile


class ParticlePackage(ConanFile):
    name = 'NeoGPS'
    version = 'v4.2.9'
    url = 'https://github.com/hicktech/conan-NeoGPS'
    repo_url = 'https://github.com/SlashDevin/NeoGPS.git'
    generators = 'cmake'
    settings = []
    requires = []

    def package(self):
        self.copy('*.c*', dst='src', src='src', excludes=['*Garmin*', 'examples', 'extras'])
        self.copy('*.h*', dst='include', src='src', excludes=['*Garmin*', 'examples', 'extras'])

    def source(self):
        self.run(f'git clone {self.repo_url} .')
        self.run(f'git checkout {self.version}')

    def package_info(self):
        self.cpp_info.srcdirs = ['src']
