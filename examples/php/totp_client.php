<?php

    require_once('otphp/lib/otphp.php');

    $key = "R3A7PZLCUQIJFUGX";

    $totp = new \OTPHP\TOTP($key, array('interval' => 90));

    print $totp->now() . "\n";

?>
