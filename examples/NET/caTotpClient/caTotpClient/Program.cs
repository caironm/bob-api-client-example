using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

using OTPNet;

namespace caTotpClient
{
    class Program
    {
        static void Main(string[] args)
        {
            var totp = new OTPNet.TOTP("R3A7PZLCUQIJFUGX");

            var code = totp.now();

            Console.WriteLine(code);
        }
    }
}
