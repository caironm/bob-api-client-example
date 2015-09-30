<?php

    // This is the url to the confirmation method for the QA environment
    $url = "https://1-dot-dazzling-rex-760.appspot.com/_ah/api/bob/v1/bob/confirmation";

    /* These two variables will be sent in custom headers in every requesto to Bob,
       they are unique for Orienta, the BobKey will be different in production */
    $bobuniversity = "udlaecuador";
    $bobkey = "204f3ca7-a67f-486e-a0ab-e235a7f42cb9";

    $headers = array(
      'Accept: application/json',
      'Content-Type: application/json',
      "BobUniversity: $bobuniversity",
      "BobKey: $bobkey"
    );

    /* This Portfolio ID will be provided by the response of the Create Account method, 
       if the account was successfully created in Orienta systems the messages should 
       be "ACEPTADO" just like the example below, if for whatever reason the account is not 
       created the message value should be "RECHAZADO", the reasons can be stated in the 
       "Reason" field as an array of strings */
    $portfolioid = "1234567890";

    $reason = array(
    	'This is used if the account is rejected message="RECHAZADO"'
    );

    $data = json_encode(array(
       'Message'               => 'ACEPTADO',
       'PortfolioID'           => $portfolioid,
       'Reason'                => $reason,
       'Origin'                => $bobuniversity
    ));

    // boilerplate code to invoke the service
    function CallAPI($method, $url, $data, $headers) {
        $curl = curl_init();

        curl_setopt($curl, CURLOPT_HTTPAUTH, CURLAUTH_BASIC);
        curl_setopt($curl, CURLOPT_POST, true);
        curl_setopt($curl, CURLOPT_URL, $url);
        curl_setopt($curl, CURLOPT_HTTPHEADER, $headers);
        curl_setopt($curl, CURLOPT_POSTFIELDS, $data);
        curl_setopt($curl, CURLOPT_RETURNTRANSFER, true);
        curl_setopt($curl, CURLOPT_SSL_VERIFYHOST, false);
        curl_setopt($curl, CURLOPT_SSL_VERIFYPEER, false);

        $result = curl_exec($curl);

        curl_close($curl);

        return $result;
    }

    /* This call is the conclusion of the process, signals Bob to end its inner processes regarding the
       account creation, it doesn't return anything */
    $resp = CallAPI("POST", $url, $data, $headers);

    // This is merely used for debugging locally, can be safely removed
    var_dump($resp);

?>
