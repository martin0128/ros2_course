from setuptools import setup
import os
from glob import glob

package_name = 'ros2_course'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Include all launch files.
        (os.path.join('share', package_name),
            glob('launch/*launch.[pxy][yma]*'))
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ros_user',
    maintainer_email='ros_user@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'hello = ros2_course.hello:main',
            'turtlebot_controller = ros2_course.turtlebot_controller:main'
        ],
    },
)
