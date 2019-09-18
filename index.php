
<?php
if (isset($_POST['ON']))
{
exec("sudo python /home/pi/on.py");
}
if (isset($_POST['OFF']))
{
exec("sudo python /home/pi/off.py");
}
?>