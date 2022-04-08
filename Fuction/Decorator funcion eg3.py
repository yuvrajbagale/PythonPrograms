
def marriagedecor(func):
    def inner():
        print('Hair decoration')
        print('Face Decoration With Platinum packege')
        print('Fair and Lovly etc..')
    return inner

def getready():
    print("Ready for the marrige")

decoreted_getready=marriagedecor(getready)

decoreted_getready()