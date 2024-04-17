import java.net.HttpURLConnection;
import java.net.URL;

public class SignIn {
    //Runs signIn.py and only continues once it has finished running
    public static void runPython() {
        PythonFileHelpers.writeToFile(AppConstants.paths.SIGN_IN_FINISHED_PATH, "false");
        PythonFileHelpers.runPython(AppConstants.program.PYTHON_TYPE + " " + AppConstants.paths.SIGN_IN_PATH);

        while (true) {
            if (PythonFileHelpers.readFileFirstLine(AppConstants.paths.SIGN_IN_FINISHED_PATH, "true")) {
                break;
            }
        }
    }

    //Confirms whether there is data available for the current manager ID
    public static boolean checkDetails(String managerId) {
        //Checks if the entered Manager ID is an integer as it should be
        try {
            Integer.parseInt(managerId);
        } catch (NumberFormatException notInteger) {
            return false;
        }
        //Returns whether data is found for the Manager ID
        return getAPIResponse("https://fantasy.premierleague.com/api/entry/" + managerId + "/");
    }

    //Returns whether data is found for the Manager ID
    public static boolean getAPIResponse(String urlStr){
        try {
            //Gets response code for URL
            //https://stackoverflow.com/questions/6467848/how-to-get-http-response-code-for-a-url-in-java
            URL url = new URL(urlStr);
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.connect();
            connection.getPermission();
            return connection.getResponseCode() != 404;
        } catch (Exception ignored) {
            return false;
        }
    }
}
