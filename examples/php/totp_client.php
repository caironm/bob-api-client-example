<?php

    require_once('otphp/lib/otphp.php');

    $key = "R3A7PZLCUQIJFUGX";

    $totp = new \OTPHP\TOTP($key);

    echo $totp->now();

?>
