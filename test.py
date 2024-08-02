import subprocess
from colorama import Fore, Style, init

# Initialize Colorama
init()

# Define the colored text
text = '''     

#   .----------------.  .----------------.  .----------------.  .----------------. 
#  | .--------------. || .--------------. || .--------------. || .--------------. |
#  | |  _________   | || |  _______     | || |     _____    | || |     ____     | |
#  | | |  _   _  |  | || | |_   __ \    | || |    |_   _|   | || |   .'    `.   | |
#  | | |_/ | | \_|  | || |   | |__) |   | || |      | |     | || |  /  .--.  \  | |
#  | |     | |      | || |   |  __ /    | || |      | |     | || |  | |    | |  | |
#  | |    _| |_     | || |  _| |  \ \_  | || |     _| |_    | || |  \  `--'  /  | |
#  | |   |_____|    | || | |____| |___| | || |    |_____|   | || |   `.____.'   | |
#  | |              | || |              | || |              | || |              | |
#  | '--------------' || '--------------' || '--------------' || '--------------' |
#   '----------------'  '----------------'  '----------------'  '----------------' 

  
 '''

# Print the text with colors
print(Fore.BLUE + text + Style.RESET_ALL)
text2 = '''     
  
/***
 *      ___     __ __ _     __    __                __ _                 __                                                                            
 *     <  /    / // /(_)___/ /___/ /___  ___    ___/ /(_)____ ___  ____ / /_ ___   ____ __ __                                                          
 *     / /_   / _  // // _  // _  // -_)/ _ \  / _  // // __// -_)/ __// __// _ \ / __// // /                                                          
 *    /_/(_) /_//_//_/ \_,_/ \_,_/ \__//_//_/  \_,_//_//_/   \__/ \__/ \__/ \___//_/   \_, /                                                           
 *                                                                                    /___/                                                            
 *       ___       _      __               __ ___                        ____                                                                          
 *      |_  |     | | /| / /___   ____ ___/ // _ \ ____ ___  ___  ___   / __/____ ___ _ ___                                                            
 *     / __/ _    | |/ |/ // _ \ / __// _  // ___// __// -_)(_-< (_-<  _\ \ / __// _ `// _ \                                                           
 *    /____/(_)   |__/|__/ \___//_/   \_,_//_/   /_/   \__//___//___/ /___/ \__/ \_,_//_//_/                                                           
 *                                                                                                                                                     
 *       ____      ___                                        __  ___              __             ____                                                 
 *      |_  /     / _ \ ___ _ ___  ___ _    __ ___   ____ ___/ / / _ ) ____ __ __ / /_ ___  ____ / __/___   ____ ____ ___                              
 *     _/_ < _   / ___// _ `/(_-< (_-<| |/|/ // _ \ / __// _  / / _  |/ __// // // __// -_)/___// _/ / _ \ / __// __// -_)                             
 *    /____/(_) /_/    \_,_//___//___/|__,__/ \___//_/   \_,_/ /____//_/   \_,_/ \__/ \__/     /_/   \___//_/   \__/ \__/                              
 *                                                                                                                                                     
 *      ____      ____ ____    __     ____ _  __    __ ____ _____ ______ ____ ____   _  __  ____                                                       
 *     / / /     / __// __ \  / /    /  _// |/ /__ / // __// ___//_  __//  _// __ \ / |/ / / __/____ ___ _ ___                                         
 *    /_  _/_   _\ \ / /_/ / / /__  _/ / /    // // // _/ / /__   / /  _/ / / /_/ //    / _\ \ / __// _ `// _ \                                        
 *     /_/ (_) /___/ \___\_\/____/ /___//_/|_/ \___//___/ \___/  /_/  /___/ \____//_/|_/ /___/ \__/ \_,_//_//_/                                        
 *                                                                                                                                                     
 *       ____      _      __      __     ____                            ____                                                                          
 *      / __/     | | /| / /___  / /    / __/___  ____ _  __ ___  ____  / __/____ ___ _ ___                                                            
 *     /__ \ _    | |/ |/ // -_)/ _ \  _\ \ / -_)/ __/| |/ // -_)/ __/ _\ \ / __// _ `// _ \                                                           
 *    /____/(_)   |__/|__/ \__//_.__/ /___/ \__//_/   |___/ \__//_/   /___/ \__/ \_,_//_//_/                                                           
 *                                                                                                                                                     
 *                                                                                                                                                     
 *                                                                                                                                                     
 *                                                                                                                                                     
 *     ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____ ____
 *    /___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___//___/
 */
                                                                                                        
 '''
text3 = ''' 
                                                                                                                                           
        _      __               __ ___                        ____                                                                          
       | | /| / /___   ____ ___/ // _ \ ____ ___  ___  ___   / __/____ ___ _ ___                                                            
       | |/ |/ // _ \ / __// _  // ___// __// -_)(_-< (_-<  _\ \ / __// _ `// _ \                                                           
       |__/|__/ \___//_/   \_,_//_/   /_/   \__//___//___/ /___/ \__/ \_,_//_//_/                                                           
                                                                                              
                                                                                              '''
text4 = '''
                __ __ _     __    __                __ _                 __                                                                            
               / // /(_)___/ /___/ /___  ___    ___/ /(_)____ ___  ____ / /_ ___   ____ __ __                                                          
              / _  // // _  // _  // -_)/ _ \  / _  // // __// -_)/ __// __// _ \ / __// // /                                                          
             /_//_//_/ \_,_/ \_,_/ \__//_//_/  \_,_//_//_/   \__/ \__/ \__/ \___//_/   \_, /                                                           
                                                                                      /___/  

          '''    
          
textsql= '''
          
                  ____ ____    __     ____ _  __    __ ____ _____ ______ ____ ____   _  __                                                       
                 / __// __ \  / /    /  _// |/ /__ / // __// ___//_  __//  _// __ \ / |/ /                                         
                _\ \ / /_/ / / /__  _/ / /    // // // _/ / /__   / /  _/ / / /_/ //    /                                        
               /___/ \___\_\/____/ /___//_/|_/ \___//___/ \___/  /_/  /___/ \____//_/|_/  
          
         '''  
         
textserver='''
                   _      __      __     ____                            ____                                                                          
                  | | /| / /___  / /    / __/___  ____ _  __ ___  ____  / __/____ ___ _ ___                                                            
                  | |/ |/ // -_)/ _ \  _\ \ / -_)/ __/| |/ // -_)/ __/ _\ \ / __// _ `// _ \                                                           
                  |__/|__/ \__//_.__/ /___/ \__//_/   |___/ \__//_/   /___/ \__/ \_,_//_//_/  
      

           '''  
textpass='''                                                                                                                                                  
                   ___                                        __  ___              __             ____                                                 
                  / _ \ ___ _ ___  ___ _    __ ___   ____ ___/ / / _ ) ____ __ __ / /_ ___  ____ / __/___   ____ ____ ___                              
                 / ___// _ `/(_-< (_-<| |/|/ // _ \ / __// _  / / _  |/ __// // // __// -_)/___// _/ / _ \ / __// __// -_)                             
                /_/    \_,_//___//___/|__,__/ \___//_/   \_,_/ /____//_/   \_,_/ \__/ \__/     /_/   \___//_/   \__/ \__/  

          '''                                                                                                                                                                                        
                                                                                              

# Print the text with colors
print(Fore.GREEN + text2 + Style.RESET_ALL)
ivalue = int(input("Enter the Value: "))
if ivalue == 1:
    print(Fore.RED + text4 + Style.RESET_ALL)
    url = input("Enter the target URL:")
    out = subprocess.run(["dirb",url])
    print(out)  
elif ivalue == 2:
    print(Fore.RED + text3 + Style.RESET_ALL)
    url = input("Enter the target URL:")
    out = subprocess.run(["wpscan" ,"--url",url,"-e","u,vp","--api-token","0voifgs6LNamMwiooQIcnBLncaBj6iKTzb05KaAQklY","--random-user-agent"],capture_output=True,text=True)
    fdtxt = out.stdout.find("[+]")
    print("""\nFinal Result:\n______________________________________________________________________________________________________________________________________________________________________________________________________\n""")
    print(out.stdout[int(fdtxt):])
elif ivalue == 3:
    print(Fore.RED + textpass + Style.RESET_ALL)
    target = input("Enter the target IP or domain: ")
    user_list = "/usr/share/wordlists/usernames.txt"  # Adjust path if necessary
    pass_list = "/usr/share/wordlists/rockyou.txt"
    try:
        out = subprocess.run(["hydra", "-L", user_list, "-P", pass_list, target, "ssh"], capture_output=True, text=True)
        print(out.stdout)
        if out.stderr:
            print("Error:", out.stderr)
    except FileNotFoundError:
        print("The 'hydra' command is not found. Please make sure it's installed.")
elif ivalue == 4:
    print(Fore.RED + textsql + Style.RESET_ALL)
    url = input("Enter the target URL: ")
    try:
        out = subprocess.run(["sqlmap", "-u", url, "--batch"], capture_output=True, text=True)
        fdtxt = out.stdout.find("starting")
        print(out.stdout[int(fdtxt):])
        if out.stderr:
            print("Error:", out.stderr)
    except FileNotFoundError:
        print("The 'sqlmap' command is not found. Please make sure it's installed.")
elif ivalue == 5:
    print(Fore.RED + textserver + Style.RESET_ALL)
    url = input("Enter the target URL: ")
    out = subprocess.run(["nikto", "-h", url])
    print(out)
else:
    print("Invalid selection. Please enter correct option")

