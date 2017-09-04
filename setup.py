from distutils.core import setup
import setup_translate

pkg = 'Extensions.ManagerAutofs'
setup (name = 'enigma2-plugin-extensions-managerautofs',
       version = '1.35',
       description = 'manage autofs files',
       packages = [pkg],
       package_dir = {pkg: 'plugin'},
       package_data = {pkg: ['*.png', 'locale/*.pot', 'locale/*/LC_MESSAGES/*.mo']},
       cmdclass = setup_translate.cmdclass, # for translation
      )
