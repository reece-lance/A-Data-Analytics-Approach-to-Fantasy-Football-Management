import java.io.File;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Objects;
import java.util.Scanner;


public class PythonFileHelpers {
    //Attempts to run any program
    public static void runPython(String command) {
        try {
            Runtime.getRuntime().exec(command);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

    //Opens, writes string parameter and closes file
    public static void writeToFile(String fileName, String string) {
        try {
            FileWriter myWriter = new FileWriter(fileName);
            myWriter.write(string);
            myWriter.close();
        } catch (Exception ignored) {}
    }

    //Reads first line in fileName and checks if it equals the string parameter
    public static boolean readFileFirstLine(String fileName, String string) {
        try {
            Scanner myReader = new Scanner(new File(fileName));
            //If file not empty
            if (myReader.hasNextLine()) {
                //Checks if line equals string parameter
                if (Objects.equals(myReader.nextLine(), string)) {
                    return true;
                }
            }
            myReader.close();
        } catch (FileNotFoundException ignored) {}
        return false;
    }
}