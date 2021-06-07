from common.saveLogsToFile import saveLogsToFile
from resources.logs import getLogs
from resources.client.inputPage import index
from settings import app
from config import serverPort

app.route('/')(index)
app.route('/logs')(getLogs)

# saveLogsToFile()

if __name__ == '__main__':
    app.run(port=serverPort, host='0.0.0.0')
