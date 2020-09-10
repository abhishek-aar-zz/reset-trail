from winregistry import WinRegistry as Reg

# These are the registry values which must be deleted from windows registry filw in order to reset the trail
class regValue:
    du_meter = "HKEY_CURRENT_USER\\SOFTWARE\\Classes\\WOW6432Node\\CLSID\\{DB45000A-9764-11D6-819E-005056C00008}\\LocalServer32"
    internet_download_manager = "HKEY_USERS\\S-1-5-21-404113928-2897473447-338820518-1001_Classes\\WOW6432Node\\CLSID\\{07999AC3-058B-40BF-984F-69EB1E554CA7}"


class CleanReg:
    # Call the Reg instance
    r = Reg()

    def resetTrail(self, software):
        try:
            # trying to delete the value from the registry
            self.r.delete_key(software)
            print("--- Congrats, your trail period has been reset")
        except:
            # if something comeuo, then the resetting was unsuccessful
            print(
                f"--- Sorry. The following could be the reason:"
                "\n\t1. You dont have {software}"
                "\n\t2. Already has been reset"
            )

    # The below function is gonna delete every registry value which are given in the regValue class.
    def callMe(self):
        print("Resetting trail period of these softwares:")
        keys = [attr for attr in dir(regValue) if not attr.startswith("__")]
        for i in range(len(keys)):
            print(f"{i+1}. {keys[i]}")
            self.resetTrail(getattr(regValue(), keys[i]))


if __name__ == "__main__":
    CleanReg().callMe()
