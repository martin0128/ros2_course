# ros2_course
A feladat elvégzéshez először végrehajtottam a kötelező programoknál lévő TurtleBot3 ROS Tutorialnál lévő lépéseket.
## Környezet
Ezek sorra:
  * Elsőre végrehajtottuk a setup.bash fájlt --> source  /opt/ros/foxy/setup.bash
  * Ezután beállítottuk a modeljét a turtlebotnak --> export TURTLEBOT3_MODEL=burger
  * Majd felállítottuk a gazebo modelt --> export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:`ros2 pkg \
                                          prefix turtlebot3_gazebo \
                                          `/share/turtlebot3_gazebo/models/
  * Végül elindítottuk a szimulációs világot --> ros2 launch turtlebot3_gazebo empty_world.launch.py
 ## Mozgatás
 Miután elindult a gazebo a teknős irányítása volt a fő cél, ez eleinte a billentyűzettel teljesen elegendő volt:
  * Turtlebot model beállítása --> export TURTLEBOT3_MODEL=burger
  * Billentyűzet használata a mozgatáshoz --> ros2 run turtlebot3_teleop teleop_keyboard
 ## Script
 A következő feladat egy script írása volt, mely automatikusan irányatja a teknőst, akadályokat elkerülve. Ennek megírására használtam segítségül a chatGPT, mely kiadott egy majdnem jó kódot, azonban néhány apró változtatásra szükség volt:
  * Először is a teknső nagyon lassan mozgott, így annak sebességét feljebb vettem --> cmd_vel.linear.x = 0.5
  * A második hibája az volt, hogy csak folyamatosan forgott ha meglátta a tárgyat amit ki kéne kerüljön, ehhez azt kellett átírni, hogy a szenzor látásköréből kivegye az elemet
  * Ezen kívül kisebb változtatásokat végeztem csak a kódon, de a fő logika működött

## Launch
Ezek után egy launch fájl elkészítése volt a célom, mely egyszerre elindítja a gazebot és a scriptet.
Ennél annyi feladatom volt, hogy egy LaunchDescriptionbe beletegyem a gazebo fájlt, elérési úttal együtt, és a végrehajtandó scriptet és a packaget ami van.
