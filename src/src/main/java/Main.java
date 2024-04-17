import com.formdev.flatlaf.FlatLightLaf;

public class Main {
    public static void main(String[] args) {
        FlatLightLaf.setup();

        PythonFileHelpers.writeToFile(AppConstants.paths.PYTHON_MAIN_FINISHED_PATH, "false");
        PythonFileHelpers.runPython(AppConstants.program.PYTHON_TYPE + " " + AppConstants.paths.PYTHON_MAIN_PATH);

        while (true) {
            if (PythonFileHelpers.readFileFirstLine(AppConstants.paths.PYTHON_MAIN_FINISHED_PATH, "true")) {
                break;
            }
        }
        try {
            new GUI().initialise();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}