import json

class HandleLocalData:
    playerFiles = ["forwards.json", "midfielders.json", "defenders.json", "goalkeepers.json"]
    
    def saveData(self, data, pos):
        # Save data to local storage
        with open(HandleLocalData.playerFiles[pos], "w") as outfile:
            json.dump(data, outfile)
        outfile.close()
        print("Data saved to local storage")
        
    
    def loadData(self, pos):
        # Load data from local storage
        with open(HandleLocalData.playerFiles[pos], "r") as openFile:
            data = json.load(openFile)
        openFile.close()
        return data
