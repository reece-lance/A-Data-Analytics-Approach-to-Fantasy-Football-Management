import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;

import java.io.FileReader;
import java.util.ArrayList;
import java.util.LinkedHashMap;

public class DataTable {
    public ArrayList<LinkedHashMap<String, String>> readJson(String fileDir, String[] columnHeaders) {
        JSONParser parser = new JSONParser();
        try {
            JSONArray jsonArray = (JSONArray) parser.parse(new FileReader(fileDir));
            ArrayList<LinkedHashMap<String, String>> tableValues = new ArrayList<>();
            for (Object arrObject : jsonArray) {
                JSONObject object = (JSONObject) arrObject;
                LinkedHashMap<String, String> row = new LinkedHashMap<>();
                for (String columnHeader : columnHeaders) {
                    row.put(columnHeader, String.valueOf(object.get(columnHeader)));
                }
                tableValues.add(row);
            }
            return tableValues;
        } catch (Exception ignored) {
        }
        return null;
    }
}