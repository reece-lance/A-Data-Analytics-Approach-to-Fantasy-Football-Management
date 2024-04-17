import java.io.File;

public class AppConstants {
    public static class directories {
        public static final String CWD_PARENT_DIR = new File(System.getProperty("user.dir")).getParent(); //>-1
        public static final String IMAGES_DIR = CWD_PARENT_DIR + "/images"; //>-0
        public static final String PYTHON_DIR = CWD_PARENT_DIR + "/python"; //>-0
        public static final String STORED_DATA_DIR = PYTHON_DIR + "/stored_data"; //>1
        public static final String TABLES_DIR = PYTHON_DIR + "/tables"; //>-2

        public static final String PREDICTIONS_DIR = STORED_DATA_DIR + "/predictions"; //>2
        public static final String PREDICTIONS_HISTORY_DIR = PREDICTIONS_DIR + folders.HISTORY_FOLDER; //>3
        public static final String PREDICTIONS_TEAMS_DIR = PREDICTIONS_DIR + folders.TEAMS_FOLDER; //>3

        public static final String SIGN_IN_DIR = STORED_DATA_DIR + "/signInData"; //>2
        public static final String SIGN_IN_HISTORY_DIR = SIGN_IN_DIR + folders.HISTORY_FOLDER; //>3
        public static final String SIGN_IN_TEAMS_DIR = SIGN_IN_DIR + folders.TEAMS_FOLDER; //>3
    }
    public static class folders {
        public static final String HISTORY_FOLDER = "/history";
        public static final String TEAMS_FOLDER = "/teams";
    }

    public static class fileNames {
        public static final String GAMEWEEK_FILE_NAME = "/gameweek-{gameweek}.json";
        public static final String LOGW_FILE_NAME = "/list-of-gameweeks.json";
        public static final String MANAGER_BASIC_FILE_NAME = "/manager-basic-info.json";
        public static final String MANAGER_SECURITY_FILE_NAME = "/manager-security.json";
    }
    public static class paths {
        public static final String PYTHON_MAIN_PATH = directories.PYTHON_DIR + "/main.py"; //>1
        public static final String PYTHON_MAIN_FINISHED_PATH = directories.PYTHON_DIR + "/mainFinished.json"; //>1
        public static final String SIGN_IN_PATH = directories.PYTHON_DIR + "/signIn.py"; //>1
        public static final String SIGN_IN_FINISHED_PATH = directories.PYTHON_DIR + "/signInFinished.json"; //>1

        public static final String PREDICTIONS_LOGW_PATH = directories.PREDICTIONS_DIR + fileNames.LOGW_FILE_NAME; //>3
        public static final String PRED_MANAGER_BASICS_PATH = directories.PREDICTIONS_DIR + fileNames.MANAGER_BASIC_FILE_NAME; //>3
        public static final String PREDICTIONS_HISTORY_PATH = directories.PREDICTIONS_HISTORY_DIR + fileNames.GAMEWEEK_FILE_NAME; //>4
        public static final String PREDICTIONS_TEAMS_PATH = directories.PREDICTIONS_TEAMS_DIR + fileNames.GAMEWEEK_FILE_NAME; //>4

        public static final String SIGN_IN_LOGW_PATH = directories.SIGN_IN_DIR + fileNames.LOGW_FILE_NAME; //>3
        public static final String SIGN_IN_MANAGER_BASICS_PATH = directories.SIGN_IN_DIR + fileNames.MANAGER_BASIC_FILE_NAME; //>3
        public static final String SIGN_IN_MANAGER_SECURITY_PATH = directories.SIGN_IN_DIR + fileNames.MANAGER_SECURITY_FILE_NAME; //>3
        public static final String SIGN_IN_HISTORY_PATH = directories.SIGN_IN_HISTORY_DIR + fileNames.GAMEWEEK_FILE_NAME; //>4
        public static final String SIGN_IN_TEAMS_PATH = directories.SIGN_IN_TEAMS_DIR + fileNames.GAMEWEEK_FILE_NAME; //>4

        public static final String PLAYERS_TABLE_PATH = directories.TABLES_DIR + "/playersTable.json"; //>3
        public static final String LEAGUE_TABLE_PATH = directories.TABLES_DIR + "/leagueTable.json"; //>3
        public static final String FIXTURE_TABLE_PATH = directories.TABLES_DIR + "/fixtureTable.json"; //>3
        public static final String RESULTS_TABLE_PATH = directories.TABLES_DIR + "/resultsTable.json"; //>3

        public static final String PL_LOGO_GREEN = directories.IMAGES_DIR + "/pl_logo_green.png";
        public static final String PL_LOGO_PURPLE = directories.IMAGES_DIR + "/pl_logo_purple.png";
    }
    public static class urls {
        public static final String PLAYER_IMAGE_URL = "https://resources.premierleague.com/premierleague/photos/players/110x140/p";
    }
    public static class program {
        public static final String PYTHON_TYPE = "Python3";
    }
}