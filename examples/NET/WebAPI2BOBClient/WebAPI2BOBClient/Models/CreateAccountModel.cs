using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace WebAPI2BOBClient.Models
{
    class CreateAccountModel
    {
        public string Agreement { get; set; }
        public string EmailAddress { get; set; }
        public string FirstName { get; set; }
        public string MaternalLastName { get; set; }
        public string PaternalLastName { get; set; }
        public string PhoneNumber { get; set; }
        public string UserName { get; set; }
        public string Password { get; set; }
        public string Origin { get; set; }
        public string GradeNumber { get; set; }
    }
}
