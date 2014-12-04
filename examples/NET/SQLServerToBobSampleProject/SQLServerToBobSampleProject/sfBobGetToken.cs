//------------------------------------------------------------------------------
// <copyright file="CSSqlFunction.cs" company="Microsoft">
//     Copyright (c) Microsoft Corporation.  All rights reserved.
// </copyright>
//------------------------------------------------------------------------------
using System;
using System.Data;
using System.Data.SqlClient;
using System.Data.SqlTypes;
using Microsoft.SqlServer.Server;

using OTPNet;

public partial class UserDefinedFunctions
{
    [Microsoft.SqlServer.Server.SqlFunction]
    public static SqlString sfBobGetToken()
    {
        // Put your code here
        var totp = new OTPNet.TOTP("R3A7PZLCUQIJFUGX");

        var code = totp.now();

        return new SqlString(code.ToString());
    }
}
