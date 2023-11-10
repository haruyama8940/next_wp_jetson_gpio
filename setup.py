from setuptools import find_packages, setup

package_name = 'next_wp_jetson_gpio'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='haru',
    maintainer_email='yaruo0406@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'next_wp_jetson_gpio_node = next_wp_jetson_gpio.send_next_wp:main'
        ],
    },
)
