import com.formdev.flatlaf.FlatDarculaLaf;
import com.formdev.flatlaf.FlatLaf;
import com.formdev.flatlaf.FlatLightLaf;
import org.json.simple.JSONArray;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import javax.imageio.ImageIO;
import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.io.FileReader;
import java.io.IOException;
import java.net.URL;
import java.util.*;

public class GUI {
    private JPanel mainPanel;
    private JTabbedPane mainTabbedPane;
    private JButton signInButton;
    private JTable myGameweekTable;
    private JTable resultsTable;
    private JTable playersTable;
    public JTable leagueTableTable;
    private JLabel logoLabel;
    private JLabel titleLabel;
    private JScrollPane playersScrollPanel;
    private JScrollPane resultsScrollPane;
    private JPanel resultsPanel;
    private JPanel leagueTablePanel;
    private JScrollPane leagueTableScrollPane;
    private JTable fixturesTable;
    private JPanel fixturesPanel;
    private JScrollPane fixturesScrollPane;
    private JPanel playersPanel;
    private JTextField managerIdField;
    private JButton colourModeButton;
    private JLabel managerIdLbl;
    private JPasswordField passwordField;
    private JTextField usernameField;
    private JCheckBox previousDetailsCheckBox;
    private JTabbedPane teamsPanel;
    private JLabel def3Pos1Team;
    private JLabel gkPos;
    private JLabel gkIcon;
    private JLabel gkSpecial;
    private JLabel def3Pos1Pos;
    private JLabel def3Pos1Icon;
    private JLabel def3Pos1Special;
    private JLabel def3Pos2Pos;
    private JLabel def3Pos2Icon;
    private JLabel def3Pos2Special;
    private JLabel def3Pos3Pos;
    private JLabel def3Pos3Icon;
    private JLabel def3Pos3Special;
    private JLabel def4Pos1Pos;
    private JLabel def4Pos1Icon;
    private JLabel def4Pos1Special;
    private JLabel def4Pos2Pos;
    private JLabel def4Pos2Icon;
    private JLabel def4Pos2Special;
    private JLabel def4Pos3Pos;
    private JLabel def4Pos3Icon;
    private JLabel def4Pos3Special;
    private JLabel def4Pos4Icon;
    private JLabel def4Pos4Special;
    private JLabel def5Pos1Pos;
    private JLabel def5Pos1Icon;
    private JLabel def5Pos1Special;
    private JLabel def5Pos2Pos;
    private JLabel def5Pos2Icon;
    private JLabel def5Pos2Special;
    private JLabel def5Pos3Pos;
    private JLabel def5Pos3Icon;
    private JLabel def5Pos3Special;
    private JLabel def5Pos4Icon;
    private JLabel def5Pos4Special;
    private JLabel def5Pos5Icon;
    private JLabel def5Pos5Special;
    private JLabel mid2Pos1Pos;
    private JLabel mid2Pos1Icon;
    private JLabel mid2Pos1Special;
    private JLabel mid2Pos2Pos;
    private JLabel mid2Pos2Icon;
    private JLabel mid2Pos2Special;
    private JLabel mid3Pos1Pos;
    private JLabel mid3Pos1Icon;
    private JLabel mid3Pos1Special;
    private JLabel mid3Pos2Pos;
    private JLabel mid3Pos2Icon;
    private JLabel mid3Pos2Special;
    private JLabel mid3Pos3Pos;
    private JLabel mid3Pos3Icon;
    private JLabel mid3Pos3Special;
    private JLabel mid4Pos1Pos;
    private JLabel mid4Pos1Icon;
    private JLabel mid4Pos1Special;
    private JLabel mid4Pos2Pos;
    private JLabel mid4Pos2Icon;
    private JLabel mid4Pos2Special;
    private JLabel mid4Pos3Pos;
    private JLabel mid4Pos3Icon;
    private JLabel mid4Pos3Special;
    private JLabel mid4Pos4Icon;
    private JLabel mid4Pos4Special;
    private JLabel mid5Pos1Pos;
    private JLabel mid5Pos1Icon;
    private JLabel mid5Pos1Special;
    private JLabel mid5Pos2Pos;
    private JLabel mid5Pos2Icon;
    private JLabel mid5Pos2Special;
    private JLabel mid5Pos3Pos;
    private JLabel mid5Pos3Icon;
    private JLabel mid5Pos3Special;
    private JLabel mid5Pos4Icon;
    private JLabel mid5Pos4Special;
    private JLabel mid5Pos5Icon;
    private JLabel mid5Pos5Special;
    private JLabel for1Pos1Pos;
    private JLabel for1Pos1Icon;
    private JLabel for1Pos1Special;
    private JLabel for2Pos1Pos;
    private JLabel for2Pos1Icon;
    private JLabel for2Pos1Special;
    private JLabel for2Pos2Pos;
    private JLabel for2Pos2Icon;
    private JLabel for2Pos2Special;
    private JLabel for3Pos1Pos;
    private JLabel for3Pos1Icon;
    private JLabel for3Pos1Special;
    private JLabel for3Pos2Pos;
    private JLabel for3Pos2Icon;
    private JLabel for3Pos2Special;
    private JLabel for3Pos3Pos;
    private JLabel for3Pos3Icon;
    private JLabel for3Pos3Special;
    private JPanel fantasyPanel;
    private JPanel myStatsPanel;
    private JLabel subPos1Pos;
    private JLabel subPos1Icon;
    private JLabel subPos1Special;
    private JLabel subPos2Pos;
    private JLabel subPos2Icon;
    private JLabel subPos2Special;
    private JLabel subPos3Pos;
    private JLabel subPos3Icon;
    private JLabel subPos3Special;
    private JLabel subPos4Pos;
    private JLabel subPos4Icon;
    private JLabel subPos4Special;
    private JLabel gkName;
    private JLabel def3Pos1Name;
    private JLabel def3Pos2Name;
    private JLabel def3Pos3Name;
    private JLabel def4Pos1Name;
    private JLabel def4Pos2Name;
    private JLabel def4Pos3Name;
    private JLabel def4Pos4Name;
    private JLabel def5Pos1Name;
    private JLabel def5Pos2Name;
    private JLabel def5Pos3Name;
    private JLabel def5Pos4Name;
    private JLabel def5Pos5Name;
    private JLabel mid2Pos1Name;
    private JLabel mid2Pos2Name;
    private JLabel mid3Pos1Name;
    private JLabel mid3Pos2Name;
    private JLabel mid3Pos3Name;
    private JLabel mid4Pos1Name;
    private JLabel mid4Pos2Name;
    private JLabel mid4Pos3Name;
    private JLabel mid4Pos4Name;
    private JLabel mid5Pos1Name;
    private JLabel mid5Pos2Name;
    private JLabel mid5Pos3Name;
    private JLabel mid5Pos4Name;
    private JLabel mid5Pos5Name;
    private JLabel for1Pos1Name;
    private JLabel for2Pos1Name;
    private JLabel for2Pos2Name;
    private JLabel for3Pos1Name;
    private JLabel for3Pos2Name;
    private JLabel subPos1Name;
    private JLabel subPos2Name;
    private JLabel subPos3Name;
    private JLabel subPos4Name;
    private JLabel myMID2Pos1Name;
    private JPanel myDEF4Pos2;
    private JLabel myFWD3Pos1Points;
    private JPanel myDEF3;
    private JPanel myFWDPanel;
    private JLabel myDEF5Pos3Icon;
    private JLabel myDEF5Pos4Name;
    private JLabel myFWD1Pos1Icon;
    private JLabel myGKIcon;
    private JPanel myMID4;
    private JPanel myGK;
    private JLabel myDEF3Pos1Points;
    private JLabel myDEF5Pos2Special;
    private JLabel myDEF3Pos3Points;
    private JLabel myMID2Pos1Icon;
    private JLabel myDEF4Pos1Name;
    private JPanel myMID2;
    private JLabel myDEF4Pos3Icon;
    private JLabel myDEF5Pos3Special;
    private JLabel myDEF4Pos4Points;
    private JLabel myMID5Pos2Points;
    private JLabel myDEF5Pos2Points;
    private JLabel mySUB1Points;
    private JLabel myMID5Pos2Name;
    private JPanel myMID5Pos5;
    private JLabel myMID4Pos1Icon;
    private JPanel myMID2Pos2;
    private JPanel myDEF5Pos4;
    private JPanel myDEF5Pos5;
    private JLabel mySUB4Icon;
    private JLabel myMID3Pos3Icon;
    private JPanel myMID5Pos3;
    private JLabel myDEF5Pos3Name;
    private JPanel myMID4Pos2;
    private JLabel myMID3Pos1Name;
    private JLabel myDEF4Pos2Icon;
    private JLabel mySUB3Special;
    private JLabel myGKPoints;
    private JLabel myFWD2Pos2Name;
    private JLabel myDEF5Pos2Name;
    private JLabel myMID5Pos4Special;
    private JLabel myDEF5Pos1Icon;
    private JLabel myMID3Pos3Special;
    private JLabel mySUB3Name;
    private JToolBar myGameweekToolbar;
    private JPanel myDEF4Pos1;
    private JLabel myFWD1Pos1Points;
    private JLabel myMID4Pos2Icon;
    private JLabel myMID5Pos2Special;
    private JLabel mySUB4Special;
    private JLabel myMID3Pos3Name;
    private JPanel myGKPanel;
    private JLabel mySUB3Points;
    private JLabel myFWD2Pos2Special;
    private JLabel myDEF5Pos1Special;
    private JLabel mySUB1Icon;
    private JLabel myMID5Pos4Icon;
    private JLabel myFWD3Pos2Name;
    private JLabel mySUB1Special;
    private JLabel myDEF5Pos5Points;
    private JLabel myMID2Pos1Points;
    private JPanel mySUB1;
    private JLabel myFWD1Pos1Special;
    private JLabel myMID3Pos3Points;
    private JLabel myFWD3Pos3Points;
    private JLabel myDEF4Pos1Icon;
    private JLabel myDEF3Pos3Name;
    private JLabel myDEF5Pos1Points;
    private JPanel myDEFPanel;
    private JLabel myDEF4Pos2Points;
    private JLabel myDEF4Pos4Icon;
    private JPanel myDEF5Pos2;
    private JLabel myMID4Pos2Special;
    private JLabel myMID5Pos3Special;
    private JPanel myMID5;
    private JLabel myDEF4Pos4Special;
    private JLabel myMID2Pos2Points;
    private JPanel myMID3;
    private JButton myLeftButton;
    private JLabel myMID2Pos2Icon;
    private JLabel mySUB2Special;
    private JLabel myFWD2Pos2Icon;
    private JLabel myDEF4Pos3Points;
    private JLabel myMID3Pos2Special;
    private JLabel myMID4Pos4Icon;
    private JPanel myFWD2Pos2;
    private JPanel myMID2Pos1;
    private JLabel myMID4Pos1Special;
    private JPanel myMID3Pos1;
    private JPanel myMIDPanel;
    private JLabel myGKName;
    private JLabel myMID4Pos2Name;
    private JLabel myMID5Pos1Points;
    private JLabel myMID5Pos1Name;
    private JLabel myDEF4Pos3Name;
    private JLabel myMID5Pos3Name;
    private JLabel myMID5Pos5Special;
    private JLabel myFWD3Pos2Points;
    private JLabel myFWD3Pos1Special;
    private JLabel myMID2Pos1Special;
    private JLabel myDEF3Pos2Icon;
    private JLabel myMID4Pos3Special;
    private JPanel myDEF4Pos4;
    private JPanel myFWD3Pos3;
    private JPanel myFWD1Pos1;
    private JLabel myFWD3Pos3Name;
    private JPanel mySUB4;
    private JLabel myDEF3Pos2Points;
    private JLabel myFWD3Pos1Icon;
    private JLabel myMID3Pos1Icon;
    private JLabel mySUB3Icon;
    private JLabel myMID5Pos3Icon;
    private JLabel myDEF3Pos2Special;
    private JLabel myDEF4Pos1Points;
    private JPanel myMID3Pos2;
    private JLabel myDEF3Pos1Icon;
    private JLabel myMID5Pos5Points;
    private JLabel myDEF3Pos3Special;
    private JLabel myFWD1Pos1Name;
    private JPanel myFWD1;
    private JLabel myFWD2Pos1Points;
    private JLabel mySUB1Name;
    private JLabel myMID5Pos5Name;
    private JLabel mySUB2Icon;
    private JLabel myGKSpecial;
    private JButton myRightButton;
    private JPanel myDEF4Pos3;
    private JLabel mySUB2Name;
    private JPanel myDEF5Pos3;
    private JPanel myFWD3Pos2;
    private JLabel myDEF5Pos4Icon;
    private JLabel myFWD2Pos1Icon;
    private JLabel myDEF5Pos4Points;
    private JLabel myMID4Pos3Points;
    private JLabel myDEF3Pos2Name;
    private JLabel myMID3Pos2Icon;
    private JLabel myDEF4Pos4Name;
    private JLabel myMID5Pos4Points;
    private JLabel myDEF4Pos3Special;
    private JPanel mySUBPanel;
    private JLabel myMID3Pos2Points;
    private JLabel myMID5Pos1Icon;
    private JPanel myMID4Pos3;
    private JLabel myDEF5Pos3Points;
    private JLabel myMID2Pos2Name;
    private JPanel myTeamsTab;
    private JPanel myDEF3Pos2;
    private JLabel myDEF4Pos2Name;
    private JLabel myMID2Pos2Special;
    private JPanel myMID5Pos1;
    private JLabel myFWD3Pos2Special;
    private JPanel myTeamPanel;
    private JPanel myDEF5Pos1;
    private JLabel myFWD3Pos3Icon;
    private JPanel myMID5Pos4;
    private JLabel myDEF3Pos1Special;
    private JLabel myFWD2Pos1Name;
    private JLabel myMID3Pos2Name;
    private JLabel myDEF5Pos5Name;
    private JPanel myDEF3Pos3;
    private JLabel myMID3Pos1Points;
    private JLabel myMID4Pos1Name;
    private JPanel myMID5Pos2;
    private JPanel mySUB2;
    private JLabel myFWD3Pos2Icon;
    private JLabel myMID5Pos4Name;
    private JPanel myDEF4;
    private JLabel myDEF5Pos5Special;
    private JLabel myDEF4Pos1Special;
    private JLabel myDEF3Pos3Icon;
    private JLabel myMID5Pos5Icon;
    private JPanel myFWD2Pos1;
    private JLabel myDEF5Pos1Name;
    private JPanel myFWD3;
    private JLabel myMID5Pos1Special;
    private JPanel myFWD2;
    private JLabel myFWD2Pos1Special;
    private JLabel myFWD2Pos2Points;
    private JLabel myDEF4Pos2Special;
    private JTabbedPane myViewTab;
    private JPanel myFWD3Pos1;
    private JLabel myMID4Pos4Special;
    private JPanel myDEF5;
    private JLabel myMID4Pos4Name;
    private JPanel mySUB3;
    private JPanel myMID4Pos4;
    private JLabel myMID5Pos3Points;
    private JPanel myMID3Pos3;
    private JLabel myDEF5Pos5Icon;
    private JLabel myMID4Pos3Name;
    private JLabel myMID3Pos1Special;
    private JLabel myMID4Pos4Points;
    private JLabel mySUB4Points;
    private JLabel mySUB2Points;
    private JLabel myMID4Pos1Points;
    private JPanel myMID4Pos1;
    private JLabel myFWD3Pos3Special;
    private JLabel myDEF5Pos4Special;
    private JLabel myMID4Pos3Icon;
    private JLabel myFWD3Pos1Name;
    private JLabel myMID5Pos2Icon;
    private JLabel myDEF5Pos2Icon;
    private JLabel mySUB4Name;
    private JLabel myMID4Pos2Points;
    private JLabel myGameweekLabel;
    private JLabel myDEF3Pos1Name;
    private JLabel predFWD2Pos1Icon;
    private JLabel predSUB3Icon;
    private JPanel predDEF3Pos2;
    private JPanel predMID5Pos5;
    private JLabel predFWD3Pos3Points;
    private JPanel predMID5Pos3;
    private JLabel predFWD1Pos1Icon;
    private JLabel predDEF5Pos2Points;
    private JLabel predMID3Pos2Name;
    private JLabel predMID5Pos5Icon;
    private JLabel predDEF5Pos4Special;
    private JLabel predDEF4Pos1Name;
    private JLabel predFWD2Pos2Special;
    private JLabel predFWD3Pos1Name;
    private JLabel predDEF4Pos2Name;
    private JLabel predMID5Pos3Special;
    private JLabel predMID5Pos5Points;
    private JLabel predMID4Pos1Icon;
    private JPanel predGKPanel;
    private JPanel predDEF5Pos4;
    private JPanel predDEF4;
    private JLabel predMID5Pos4Points;
    private JLabel predMID2Pos1Icon;
    private JLabel predMID5Pos2Special;
    private JLabel predMID4Pos2Icon;
    private JLabel predDEF3Pos2Icon;
    private JLabel predDEF4Pos4Name;
    private JLabel predDEF3Pos1Special;
    private JLabel predDEF5Pos5Name;
    private JLabel predFWD2Pos1Name;
    private JLabel predFWD3Pos2Special;
    private JLabel predDEF5Pos4Points;
    private JLabel predFWD2Pos1Points;
    private JLabel predDEF5Pos4Icon;
    private JPanel predFWD1Pos1;
    private JLabel predDEF4Pos3Name;
    private JLabel predMID5Pos2Icon;
    private JLabel predMID5Pos1Name;
    private JLabel predFWD2Pos2Icon;
    private JLabel predMID2Pos2Icon;
    private JLabel predSUB3Special;
    private JLabel predMID3Pos1Name;
    private JPanel predDEF3Pos1;
    private JLabel predMID2Pos1Special;
    private JPanel predDEF4Pos3;
    private JLabel predDEF4Pos2Icon;
    private JPanel predMID4Pos2;
    private JLabel predFWD3Pos3Name;
    private JPanel predMID2Pos2;
    private JPanel predMID3Pos2;
    private JLabel predSUB2Icon;
    private JLabel predMID5Pos4Special;
    private JLabel predDEF3Pos2Points;
    private JLabel predDEF5Pos3Special;
    private JLabel predSUB1Name;
    private JLabel predFWD1Pos1Points;
    private JLabel predMID5Pos3Points;
    private JLabel predMID3Pos1Icon;
    private JLabel predMID5Pos2Points;
    private JLabel predFWD2Pos2Points;
    private JPanel predMID3Pos3;
    private JPanel predFWDPanel;
    private JPanel predFWD2Pos1;
    private JPanel predMID4Pos1;
    private JLabel predDEF4Pos2Special;
    private JLabel predFWD3Pos3Special;
    private JPanel predSUB1;
    private JLabel predDEF5Pos2Special;
    private JLabel predMID2Pos2Points;
    private JLabel predMID5Pos5Name;
    private JLabel predGameweekLabel;
    private JLabel predSUB2Points;
    private JLabel predDEF4Pos2Points;
    private JLabel predDEF5Pos3Points;
    private JPanel predMID5Pos1;
    private JLabel predDEF4Pos4Special;
    private JLabel predDEF5Pos1Special;
    private JLabel predMID4Pos3Points;
    private JLabel predDEF5Pos5Icon;
    private JLabel predMID5Pos3Name;
    private JLabel predDEF5Pos1Name;
    private JLabel predMID2Pos1Points;
    private JPanel predDEF4Pos2;
    private JLabel predSUB4Name;
    private JPanel predDEF5;
    private JLabel predDEF5Pos4Name;
    private JLabel predDEF4Pos4Points;
    private JPanel predDEF5Pos2;
    private JLabel predSUB3Name;
    private JTabbedPane predViewTab;
    private JLabel predDEF5Pos3Name;
    private JLabel predSUB4Special;
    private JLabel predMID4Pos2Special;
    private JLabel predSUB2Special;
    private JLabel predDEF3Pos3Name;
    private JLabel predMID4Pos3Special;
    private JLabel predSUB2Name;
    private JLabel predFWD3Pos1Points;
    private JPanel predMIDPanel;
    private JLabel predFWD3Pos2Name;
    private JLabel predMID4Pos4Points;
    private JLabel predMID5Pos2Name;
    private JLabel predMID2Pos2Name;
    private JPanel predDEF3Pos3;
    private JPanel predMID3Pos1;
    private JTable predGameweekTable;
    private JPanel predSUB3;
    private JLabel predDEF5Pos2Name;
    private JLabel predMID4Pos3Name;
    private JLabel predFWD1Pos1Special;
    private JLabel predSUB3Points;
    private JLabel predMID5Pos1Icon;
    private JLabel predDEF4Pos3Special;
    private JPanel predMID2;
    private JLabel predFWD2Pos1Special;
    private JLabel predDEF5Pos1Icon;
    private JLabel predDEF3Pos1Points;
    private JPanel predDEF3;
    private JLabel predFWD3Pos3Icon;
    private JLabel predMID5Pos3Icon;
    private JPanel predMID4Pos4;
    private JLabel predDEF5Pos2Icon;
    private JLabel predMID2Pos1Name;
    private JLabel predMID4Pos4Special;
    private JLabel predMID3Pos3Special;
    private JLabel predDEF4Pos1Points;
    private JLabel predDEF3Pos2Special;
    private JLabel predDEF3Pos3Icon;
    private JLabel predMID3Pos3Points;
    private JLabel predDEF4Pos4Icon;
    private JLabel predMID4Pos2Name;
    private JPanel predMID4;
    private JPanel predTeamPanel;
    private JPanel predDEF4Pos1;
    private JLabel predDEF5Pos5Points;
    private JLabel predFWD2Pos2Name;
    private JLabel predMID4Pos2Points;
    private JPanel predFWD3Pos1;
    private JLabel predMID4Pos1Points;
    private JLabel predFWD3Pos1Special;
    private JLabel predMID2Pos2Special;
    private JButton predRightButton;
    private JLabel predMID4Pos1Name;
    private JPanel predFWD3;
    private JPanel predFWD1;
    private JPanel predFWD2Pos2;
    private JLabel predDEF4Pos1Special;
    private JLabel predDEF4Pos3Icon;
    private JLabel predSUB1Points;
    private JLabel predMID3Pos2Points;
    private JPanel predMID2Pos1;
    private JLabel predMID3Pos3Name;
    private JPanel predMID5Pos4;
    private JLabel predFWD3Pos2Points;
    private JLabel predDEF5Pos5Special;
    private JLabel predFWD3Pos1Icon;
    private JPanel predSUB4;
    private JLabel predMID4Pos4Icon;
    private JLabel predDEF5Pos1Points;
    private JPanel predMID3;
    private JLabel predMID5Pos1Special;
    private JPanel predSUBPanel;
    private JLabel predDEF3Pos1Name;
    private JPanel predDEF5Pos1;
    private JLabel predMID3Pos2Special;
    private JLabel predGKSpecial;
    private JLabel predGKPoints;
    private JLabel predGKName;
    private JPanel predDEF4Pos4;
    private JPanel predDEF5Pos3;
    private JPanel predMID5;
    private JLabel predMID5Pos4Name;
    private JLabel predMID3Pos1Special;
    private JPanel predGK;
    private JPanel predFWD3Pos2;
    private JPanel predSUB2;
    private JLabel predMID3Pos2Icon;
    private JLabel predSUB4Points;
    private JPanel predMID5Pos2;
    private JPanel predFWD2;
    private JLabel predDEF3Pos2Name;
    private JPanel predFWD3Pos3;
    private JButton predLeftButton;
    private JLabel predMID4Pos4Name;
    private JLabel predFWD3Pos2Icon;
    private JLabel predMID3Pos3Icon;
    private JLabel predMID4Pos3Icon;
    private JLabel predSUB1Icon;
    private JPanel predDEF5Pos5;
    private JLabel predDEF4Pos3Points;
    private JLabel predDEF3Pos3Points;
    private JLabel predSUB1Special;
    private JLabel predDEF5Pos3Icon;
    private JLabel predDEF4Pos1Icon;
    private JLabel predMID5Pos4Icon;
    private JLabel Points;
    private JLabel predSUB4Icon;
    private JLabel predDEF3Pos3Special;
    private JToolBar predGameweekToolbar;
    private JLabel predDEF3Pos1Icon;
    private JLabel predMID3Pos1Points;
    private JLabel predMID5Pos1Points;
    private JLabel predFWD1Pos1Name;
    private JPanel predMID4Pos3;
    private JLabel predMID5Pos5Special;
    private JPanel predDEFPanel;
    private JLabel predGKIcon;
    private JLabel predMID4Pos1Special;
    private JPanel myPitchViewTab;
    private JPanel myListViewTab;
    private JLabel mySUB4Label;
    private JLabel mySUB3Label;
    private JLabel mySUB2Label;
    private JLabel mySUB1Label;
    private JPanel myDEF3Pos1;
    private JPanel predPitchViewTab;
    private JPanel predListViewTab;
    private JLabel predSUB4Label;
    private JLabel predSUB3Label;
    private JLabel predSUB2Label;
    private JLabel predSUB1Label;
    private JPanel myTeamsPanel;
    private JPanel predTeamsPanel;
    private JPanel predTeamsTab;
    private JLabel managerIdStatus;
    private JPanel predStatsPanel;
    private JTable predManagerDetailsTable;
    private JTable myManagerDetailsTable;
    private JTable myManagerHistoryTable;
    private JTable predManagerHistoryTable;
    private JLabel Name;

    private JLabel[][][][] myTeamLabelArray = new JLabel[][][][]{
        new JLabel[][][]{
                new JLabel[][]{
                        new JLabel[]{myGKIcon, myGKSpecial, myGKName, myGKPoints}
                }
        },
                new JLabel[][][]{
                        new JLabel[][]{
                                new JLabel[]{myDEF3Pos1Icon, myDEF3Pos1Special, myDEF3Pos1Name, myDEF3Pos1Points},
                                new JLabel[]{myDEF3Pos2Icon, myDEF3Pos2Special, myDEF3Pos2Name, myDEF3Pos2Points},
                                new JLabel[]{myDEF3Pos3Icon, myDEF3Pos3Special, myDEF3Pos3Name, myDEF3Pos3Points}
                        },
                        new JLabel[][]{
                                new JLabel[]{myDEF4Pos1Icon, myDEF4Pos1Special, myDEF4Pos1Name, myDEF4Pos1Points},
                                new JLabel[]{myDEF4Pos2Icon, myDEF4Pos2Special, myDEF4Pos2Name, myDEF4Pos2Points},
                                new JLabel[]{myDEF4Pos3Icon, myDEF4Pos3Special, myDEF4Pos3Name, myDEF4Pos3Points},
                                new JLabel[]{myDEF4Pos4Icon, myDEF4Pos4Special, myDEF4Pos4Name, myDEF4Pos4Points}
                        },
                        new JLabel[][]{
                                new JLabel[]{myDEF5Pos1Icon, myDEF5Pos1Special, myDEF5Pos1Name, myDEF5Pos1Points},
                                new JLabel[]{myDEF5Pos2Icon, myDEF5Pos2Special, myDEF5Pos2Name, myDEF5Pos2Points},
                                new JLabel[]{myDEF5Pos3Icon, myDEF5Pos3Special, myDEF5Pos3Name, myDEF5Pos3Points},
                                new JLabel[]{myDEF5Pos4Icon, myDEF5Pos4Special, myDEF5Pos4Name, myDEF5Pos4Points},
                                new JLabel[]{myDEF5Pos5Icon, myDEF5Pos5Special, myDEF5Pos5Name, myDEF5Pos5Points}
                        }
                },
                new JLabel[][][]{
                        new JLabel[][]{
                                new JLabel[]{myMID2Pos1Icon, myMID2Pos1Special, myMID2Pos1Name, myMID2Pos1Points},
                                new JLabel[]{myMID2Pos2Icon, myMID2Pos2Special, myMID2Pos2Name, myMID2Pos2Points}
                        },
                        new JLabel[][]{
                                new JLabel[]{myMID3Pos1Icon, myMID3Pos1Special, myMID3Pos1Name, myMID3Pos1Points},
                                new JLabel[]{myMID3Pos2Icon, myMID3Pos2Special, myMID3Pos2Name, myMID3Pos2Points},
                                new JLabel[]{myMID3Pos3Icon, myMID3Pos3Special, myMID3Pos3Name, myMID3Pos3Points}
                        },
                        new JLabel[][]{
                                new JLabel[]{myMID4Pos1Icon, myMID4Pos1Special, myMID4Pos1Name, myMID4Pos1Points},
                                new JLabel[]{myMID4Pos2Icon, myMID4Pos2Special, myMID4Pos2Name, myMID4Pos2Points},
                                new JLabel[]{myMID4Pos3Icon, myMID4Pos3Special, myMID4Pos3Name, myMID4Pos3Points},
                                new JLabel[]{myMID4Pos4Icon, myMID4Pos4Special, myMID4Pos4Name, myMID4Pos4Points}
                        },
                        new JLabel[][]{
                                new JLabel[]{myMID5Pos1Icon, myMID5Pos1Special, myMID5Pos1Name, myMID5Pos1Points},
                                new JLabel[]{myMID5Pos2Icon, myMID5Pos2Special, myMID5Pos2Name, myMID5Pos2Points},
                                new JLabel[]{myMID5Pos3Icon, myMID5Pos3Special, myMID5Pos3Name, myMID5Pos3Points},
                                new JLabel[]{myMID5Pos4Icon, myMID5Pos4Special, myMID5Pos4Name, myMID5Pos4Points},
                                new JLabel[]{myMID5Pos5Icon, myMID5Pos5Special, myMID5Pos5Name, myMID5Pos5Points}
                        }
                },
                new JLabel[][][]{
                        new JLabel[][]{
                                new JLabel[]{myFWD1Pos1Icon, myFWD1Pos1Special, myFWD1Pos1Name, myFWD1Pos1Points}
                        },
                        new JLabel[][]{
                                new JLabel[]{myFWD2Pos1Icon, myFWD2Pos1Special, myFWD2Pos1Name, myFWD2Pos1Points},
                                new JLabel[]{myFWD2Pos2Icon, myFWD2Pos2Special, myFWD2Pos2Name, myFWD2Pos2Points}
                        },
                        new JLabel[][]{
                                new JLabel[]{myFWD3Pos1Icon, myFWD3Pos1Special, myFWD3Pos1Name, myFWD3Pos1Points},
                                new JLabel[]{myFWD3Pos2Icon, myFWD3Pos2Special, myFWD3Pos2Name, myFWD3Pos2Points},
                                new JLabel[]{myFWD3Pos3Icon, myFWD3Pos3Special, myFWD3Pos3Name, myFWD3Pos3Points}
                        }
                },
                new JLabel[][][]{
                        new JLabel[][]{
                                new JLabel[]{mySUB1Icon, mySUB1Special, mySUB1Name, mySUB1Points},
                                new JLabel[]{mySUB2Icon, mySUB2Special, mySUB2Name, mySUB2Points},
                                new JLabel[]{mySUB3Icon, mySUB3Special, mySUB3Name, mySUB3Points},
                                new JLabel[]{mySUB4Icon, mySUB4Special, mySUB4Name, mySUB4Points}
                        }
                }
    };

    private JLabel[][][][] predTeamLabelArray = new JLabel[][][][]{
            new JLabel[][][]{
                    new JLabel[][]{
                            new JLabel[]{predGKIcon, predGKSpecial, predGKName, predGKPoints}
                    }
            },
            new JLabel[][][]{
                    new JLabel[][]{
                            new JLabel[]{predDEF3Pos1Icon, predDEF3Pos1Special, predDEF3Pos1Name, predDEF3Pos1Points},
                            new JLabel[]{predDEF3Pos2Icon, predDEF3Pos2Special, predDEF3Pos2Name, predDEF3Pos2Points},
                            new JLabel[]{predDEF3Pos3Icon, predDEF3Pos3Special, predDEF3Pos3Name, predDEF3Pos3Points}
                    },
                    new JLabel[][]{
                            new JLabel[]{predDEF4Pos1Icon, predDEF4Pos1Special, predDEF4Pos1Name, predDEF4Pos1Points},
                            new JLabel[]{predDEF4Pos2Icon, predDEF4Pos2Special, predDEF4Pos2Name, predDEF4Pos2Points},
                            new JLabel[]{predDEF4Pos3Icon, predDEF4Pos3Special, predDEF4Pos3Name, predDEF4Pos3Points},
                            new JLabel[]{predDEF4Pos4Icon, predDEF4Pos4Special, predDEF4Pos4Name, predDEF4Pos4Points}
                    },
                    new JLabel[][]{
                            new JLabel[]{predDEF5Pos1Icon, predDEF5Pos1Special, predDEF5Pos1Name, predDEF5Pos1Points},
                            new JLabel[]{predDEF5Pos2Icon, predDEF5Pos2Special, predDEF5Pos2Name, predDEF5Pos2Points},
                            new JLabel[]{predDEF5Pos3Icon, predDEF5Pos3Special, predDEF5Pos3Name, predDEF5Pos3Points},
                            new JLabel[]{predDEF5Pos4Icon, predDEF5Pos4Special, predDEF5Pos4Name, predDEF5Pos4Points},
                            new JLabel[]{predDEF5Pos5Icon, predDEF5Pos5Special, predDEF5Pos5Name, predDEF5Pos5Points}
                    }
            },
            new JLabel[][][]{
                    new JLabel[][]{
                            new JLabel[]{predMID2Pos1Icon, predMID2Pos1Special, predMID2Pos1Name, predMID2Pos1Points},
                            new JLabel[]{predMID2Pos2Icon, predMID2Pos2Special, predMID2Pos2Name, predMID2Pos2Points}
                    },
                    new JLabel[][]{
                            new JLabel[]{predMID3Pos1Icon, predMID3Pos1Special, predMID3Pos1Name, predMID3Pos1Points},
                            new JLabel[]{predMID3Pos2Icon, predMID3Pos2Special, predMID3Pos2Name, predMID3Pos2Points},
                            new JLabel[]{predMID3Pos3Icon, predMID3Pos3Special, predMID3Pos3Name, predMID3Pos3Points}
                    },
                    new JLabel[][]{
                            new JLabel[]{predMID4Pos1Icon, predMID4Pos1Special, predMID4Pos1Name, predMID4Pos1Points},
                            new JLabel[]{predMID4Pos2Icon, predMID4Pos2Special, predMID4Pos2Name, predMID4Pos2Points},
                            new JLabel[]{predMID4Pos3Icon, predMID4Pos3Special, predMID4Pos3Name, predMID4Pos3Points},
                            new JLabel[]{predMID4Pos4Icon, predMID4Pos4Special, predMID4Pos4Name, predMID4Pos4Points}
                    },
                    new JLabel[][]{
                            new JLabel[]{predMID5Pos1Icon, predMID5Pos1Special, predMID5Pos1Name, predMID5Pos1Points},
                            new JLabel[]{predMID5Pos2Icon, predMID5Pos2Special, predMID5Pos2Name, predMID5Pos2Points},
                            new JLabel[]{predMID5Pos3Icon, predMID5Pos3Special, predMID5Pos3Name, predMID5Pos3Points},
                            new JLabel[]{predMID5Pos4Icon, predMID5Pos4Special, predMID5Pos4Name, predMID5Pos4Points},
                            new JLabel[]{predMID5Pos5Icon, predMID5Pos5Special, predMID5Pos5Name, predMID5Pos5Points}
                    }
            },
            new JLabel[][][]{
                    new JLabel[][]{
                            new JLabel[]{predFWD1Pos1Icon, predFWD1Pos1Special, predFWD1Pos1Name, predFWD1Pos1Points}
                    },
                    new JLabel[][]{
                            new JLabel[]{predFWD2Pos1Icon, predFWD2Pos1Special, predFWD2Pos1Name, predFWD2Pos1Points},
                            new JLabel[]{predFWD2Pos2Icon, predFWD2Pos2Special, predFWD2Pos2Name, predFWD2Pos2Points}
                    },
                    new JLabel[][]{
                            new JLabel[]{predFWD3Pos1Icon, predFWD3Pos1Special, predFWD3Pos1Name, predFWD3Pos1Points},
                            new JLabel[]{predFWD3Pos2Icon, predFWD3Pos2Special, predFWD3Pos2Name, predFWD3Pos2Points},
                            new JLabel[]{predFWD3Pos3Icon, predFWD3Pos3Special, predFWD3Pos3Name, predFWD3Pos3Points}
                    }
            },
            new JLabel[][][]{
                    new JLabel[][]{
                            new JLabel[]{predSUB1Icon, predSUB1Special, predSUB1Name, predSUB1Points},
                            new JLabel[]{predSUB2Icon, predSUB2Special, predSUB2Name, predSUB2Points},
                            new JLabel[]{predSUB3Icon, predSUB3Special, predSUB3Name, predSUB3Points},
                            new JLabel[]{predSUB4Icon, predSUB4Special, predSUB4Name, predSUB4Points}
                    }
            }
    };

    private ArrayList<String> myGameweekArray;
    private ArrayList<String> predGameweekArray;

    private LinkedHashMap<Integer, ArrayList<LinkedHashMap<String, String>>> myStoredData;
    private LinkedHashMap<Integer, ArrayList<LinkedHashMap<String, String>>> predStoredData;

    private LinkedHashMap<JPanel, String[]> myTeamCards;
    private LinkedHashMap<JPanel, String[]> predTeamCards;

    public void initialise() {
        JFrame mainFrame = new JFrame();
        mainFrame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        mainFrame.getContentPane().add(mainPanel);

        //https://stackoverflow.com/questions/3680221/how-can-i-get-screen-resolution-in-java
        Dimension screenSize = Toolkit.getDefaultToolkit().getScreenSize();

        mainFrame.setSize((int) screenSize.getWidth(), (int) screenSize.getHeight());

        Icon plLogoGreen = new ImageIcon(AppConstants.paths.PL_LOGO_GREEN);
        Icon plLogoPurple = new ImageIcon(AppConstants.paths.PL_LOGO_PURPLE);
        logoLabel.setIcon(plLogoPurple);

        titleLabel.setFont(new Font("Quicksand", Font.PLAIN, 36));

        colourModeButton.addActionListener(e -> {
            if (Objects.equals(colourModeButton.getText(), "Dark Mode")) {
                try {
                    UIManager.setLookAndFeel(new FlatDarculaLaf());
                    changeLaF("Light Mode", plLogoGreen);
                } catch (UnsupportedLookAndFeelException ignored) {}
            }
            else if (Objects.equals(colourModeButton.getText(), "Light Mode")) {
                try {
                    UIManager.setLookAndFeel(new FlatLightLaf());
                    changeLaF("Dark Mode", plLogoPurple);
                } catch (UnsupportedLookAndFeelException ignored) {}
            }
        });

        signInButton.addActionListener(e -> {
            //Gets Manager ID entered by user
            String managerId = managerIdField.getText();
            if (SignIn.checkDetails(managerId)) { //run if there is data available for the entered Manager ID
                if (!teamsPanel.isEnabledAt(1)) {
                    //Allows access to the "My Teams" tab
                    teamsPanel.setEnabledAt(1, true);
                    //Disables tooltip on tab
                    teamsPanel.setToolTipTextAt(1, null);
                }
                //store manager ID
                PythonFileHelpers.writeToFile(AppConstants.paths.SIGN_IN_MANAGER_SECURITY_PATH, "{\"id\": \"" + managerId + "\"}");

                SignIn.runPython();

                //Initialise and refresh my team
                initialiseMyTeam();
                myStoredData = refreshManagerComponents(myStoredData, myGameweekTable, myGameweekLabel, AppConstants.paths.SIGN_IN_TEAMS_PATH, myTeamLabelArray, myTeamCards, AppConstants.paths.SIGN_IN_HISTORY_PATH, myManagerHistoryTable);
                initialiseTables(AppConstants.paths.SIGN_IN_MANAGER_BASICS_PATH,
                        new String[] {"keys", "values"},
                        new String[] {"Manager", "Stats"},
                        myManagerDetailsTable,false,
                        new Class[] {String.class, String.class},
                        new int[][] {});

                managerIdStatus.setText("Successfully logged in");
            } else {
                managerIdStatus.setText("Incorrect Manager ID");
            }
        });

        //Initialise gameweek picker for predicted team tab
        predGameweekArray = setGameweekArray(AppConstants.paths.PREDICTIONS_LOGW_PATH);
        predGameweekLabel.setText(predGameweekArray.get(predGameweekArray.size() - 1));
        changeButtonState(predGameweekArray.indexOf(predGameweekLabel.getText()), predGameweekArray.size() - 1, predRightButton, predLeftButton);

        //Initialise gameweek buttons for predicted team tab
        predLeftButton.addActionListener(e -> {
            gameweekButtonPressed(predGameweekLabel, predGameweekArray, -1, predLeftButton, predRightButton);
            predStoredData = refreshManagerComponents(predStoredData, predGameweekTable, predGameweekLabel, AppConstants.paths.PREDICTIONS_TEAMS_PATH, predTeamLabelArray, predTeamCards, AppConstants.paths.PREDICTIONS_HISTORY_PATH, predManagerHistoryTable);
        });
        predRightButton.addActionListener(e -> {
            gameweekButtonPressed(predGameweekLabel, predGameweekArray, +1, predRightButton, predLeftButton);
            predStoredData = refreshManagerComponents(predStoredData, predGameweekTable, predGameweekLabel, AppConstants.paths.PREDICTIONS_TEAMS_PATH, predTeamLabelArray, predTeamCards, AppConstants.paths.PREDICTIONS_HISTORY_PATH, predManagerHistoryTable);
        });

        //Initialise and refresh predicted team
        initialisePredTeam();
        predStoredData = refreshManagerComponents(predStoredData, predGameweekTable, predGameweekLabel, AppConstants.paths.PREDICTIONS_TEAMS_PATH, predTeamLabelArray, predTeamCards, AppConstants.paths.PREDICTIONS_HISTORY_PATH, predManagerHistoryTable);

        //Initialise predManagerDetailsTable
        initialiseTables(AppConstants.paths.PRED_MANAGER_BASICS_PATH,
                new String[] {"keys", "values"},
                new String[] {"Manager", "Stats"},
                predManagerDetailsTable,false,
                new Class[] {String.class, String.class},
                new int[][] {});

        //Initialise gameweek picker for my team tab
        myGameweekArray = setGameweekArray(AppConstants.paths.SIGN_IN_LOGW_PATH);
        myGameweekLabel.setText(myGameweekArray.get(myGameweekArray.size() - 1));
        changeButtonState(myGameweekArray.indexOf(myGameweekLabel.getText()), myGameweekArray.size() - 1, myRightButton, myLeftButton);

        //Initialise gameweek buttons for my team tab
        myLeftButton.addActionListener(e -> {
            gameweekButtonPressed(myGameweekLabel, myGameweekArray, -1, myLeftButton, myRightButton);
            myStoredData = refreshManagerComponents(myStoredData, myGameweekTable, myGameweekLabel, AppConstants.paths.SIGN_IN_TEAMS_PATH, myTeamLabelArray, myTeamCards, AppConstants.paths.SIGN_IN_HISTORY_PATH, myManagerHistoryTable);
        });
        myRightButton.addActionListener(e -> {
            gameweekButtonPressed(myGameweekLabel, myGameweekArray, +1, myRightButton, myLeftButton);
            myStoredData = refreshManagerComponents(myStoredData, myGameweekTable, myGameweekLabel, AppConstants.paths.SIGN_IN_TEAMS_PATH, myTeamLabelArray, myTeamCards, AppConstants.paths.SIGN_IN_HISTORY_PATH, myManagerHistoryTable);
        });

        //initialise players table
        initialiseTables(AppConstants.paths.PLAYERS_TABLE_PATH,
                new String[] {"second_name", "team", "element_type", "now_cost", "selected_by_percent", "form", "total_points"},
                new String[] {"Name", "Team", "Position", "Cost", "Selected By %", "Form", "Points"},
                playersTable,true,
                new Class[] {String.class, String.class, String.class, Double.class, Double.class, Double.class, Integer.class},
                new int[][] {});

        //initialise league table
        initialiseTables(AppConstants.paths.LEAGUE_TABLE_PATH,
                new String[] {"position", "badge", "team", "played", "win", "draw", "loss", "goals_for", "goals_against", "goal_difference", "points"},
                new String[] {"Position", "", "Club", "Played", "Won", "Drawn", "Lost", "GF", "GA", "GD", "Points"},
                leagueTableTable,false,
                new Class[] {Integer.class, Icon.class, String.class, Integer.class, Integer.class, Integer.class, Integer.class, Integer.class, Integer.class, Integer.class, Integer.class},
                new int[][] {});

        //initialise fixture table
        initialiseTables(AppConstants.paths.FIXTURE_TABLE_PATH,
                new String[] {"date", "time", "team_h", "badge_h", "vs", "badge_a", "team_a"},
                new String[] {"Date", "Time", "Home Team", "", "", "", "Away Team"},
                fixturesTable,false,
                new Class[] {String.class, String.class, String.class, Icon.class, String.class, Icon.class, String.class},
                new int[][] {{3, 40}, {4, 50}, {5, 40}});

        //initialise results table
        initialiseTables(AppConstants.paths.RESULTS_TABLE_PATH,
                new String[] {"date", "time", "team_h", "badge_h", "score", "badge_a", "team_a"},
                new String[] {"Date", "Time", "Home Team", "", "Score", "", "Away Team"},
                resultsTable,false,
                new Class[] {String.class, String.class, String.class, Icon.class, String.class, Icon.class, String.class},
                new int[][] {{3, 40}, {4, 50}, {5, 40}});

        mainFrame.setVisible(true);
    }

    //Changes the look and feel of the frame and changes the logo
    public void changeLaF(String text, Icon logo) {
        colourModeButton.setText(text);
        FlatLaf.updateUI();
        logoLabel.setIcon(logo);
    }

    //Refreshes components when a gameweek button is pressed
    public void gameweekButtonPressed(JLabel label, ArrayList<String> gameweekArray, int change, JButton thisButton, JButton otherButton) {
        int index = gameweekArray.indexOf(label.getText()) + change; //Applies change to gameweek counter
        //If index in range
        if (index >= 0 & index <= gameweekArray.size() - 1) {
            changeButtonState(index, gameweekArray.size() - 1, thisButton, otherButton);
        }
        else {
            index -= change; //Revert change to gameweek counter
        }
        //Change label text to new counter
        label.setText(gameweekArray.get(index));
    }

    public void changeButtonState(int index, int range, JButton thisButton, JButton otherButton) {
        //If index at the end of range
        if (index == 0 | index == range) {
            thisButton.setEnabled(false); //disable button
        }
        //If index is 1 inside the range
        else if (index == 1 | index == range - 1) {
            //If button is disabled
            if (!otherButton.isEnabled()) {
                otherButton.setEnabled(true); //Enable button
            }
        }
    }

    public ArrayList<String> setGameweekArray(String fileName) {
        JSONParser parser = new JSONParser();
        ArrayList<String> gameweekArray = new ArrayList<>();
        try {
            JSONArray jsonArray = (JSONArray) parser.parse(new FileReader(fileName));
            for (Object item : jsonArray) {
                gameweekArray.add("Gameweek " + item.toString());
            }
        } catch (IOException | ParseException e) {
            e.printStackTrace();
        }
        return gameweekArray;
    }

    public ArrayList<LinkedHashMap<String, String>> initialiseTables(String fileDir, String[] dataNames, String[] columnHeaders, JTable table, boolean autoSort, Class<?>[] classTypes, int[][] maxColumnWidths) {
        DataTable dataTable = new DataTable();
        ArrayList<LinkedHashMap<String, String>> tableList = dataTable.readJson(fileDir, dataNames);
        Object[][] tableData = insertTableData(tableList, dataNames, classTypes);
        initialiseTable(table, tableData, autoSort, columnHeaders, classTypes, maxColumnWidths);
        return tableList;
    }

    public Object[][] insertTableData(ArrayList<LinkedHashMap<String, String>> tableList, String[] dataNames, Class<?>[] classTypes) {
        Object[][] data = new Object[tableList.size()][dataNames.length];
        for (int i = 0; i < tableList.size(); i++) {
            for (int j = 0; j < dataNames.length; j++) {
                if (classTypes[j] == String.class) {
                    data[i][j] = tableList.get(i).get(dataNames[j]);
                } else if (classTypes[j] == Integer.class) {
                    try {
                        data[i][j] = Integer.parseInt(tableList.get(i).get(dataNames[j]));
                    } catch (Exception ignore) {
                        data[i][j] = 0;
                    }
                } else if (classTypes[j] == Double.class) {
                    data[i][j] = Double.valueOf(tableList.get(i).get(dataNames[j]));
                } else if (classTypes[j] == Icon.class) {
                    if (Objects.equals(dataNames[j], "photo")) {
                        data[i][j] = getPlayerImage(tableList.get(i).get(dataNames[j]), 33, 42);
                    } else {
                        data[i][j] = new ImageIcon(tableList.get(i).get(dataNames[j]));
                    }
                }
            }
        }
        return data;
    }

    public void initialiseTable(JTable table, Object[][] tableData, boolean autoSort, String[] tableColumns, Class<?>[] classTypes, int[][] maxColumnWidths) {
        DefaultTableModel tableModel = new DefaultTableModel(tableData, tableColumns) {
            Class<?>[] types = classTypes;

            @Override
            public Class<?> getColumnClass(int columnIndex) {
                return this.types[columnIndex];
            }

            public boolean isCellEditable(int row, int column) {
                return false;
            }
        };

        table.setModel(tableModel);
        customiseTable(table);
        table.setAutoCreateRowSorter(autoSort);
        for (int[] column :maxColumnWidths) {
            table.getColumnModel().getColumn(column[0]).setMaxWidth(column[1]);
        }
    }

    public LinkedHashMap<Integer, ArrayList<LinkedHashMap<String, String>>> refreshManagerComponents(LinkedHashMap<Integer, ArrayList<LinkedHashMap<String, String>>> storedData, JTable gameweekTable, JLabel gameweekLabel, String fileName, JLabel[][][][] labelArray, LinkedHashMap<JPanel, String[]> teamCards, String HistoryFileName, JTable historyTable) {
        String gameweekStr = gameweekLabel.getText().replace("Gameweek ", "");
        int gameweekInt = Integer.parseInt(gameweekStr);
        ArrayList<LinkedHashMap<String, String>> tableList;
        if (storedData.get(gameweekInt) == null) {
            tableList = initialiseTables(fileName.replace("{gameweek}", gameweekStr),
                    new String[]{"position", "photo", "name", "team_name", "position_name", "points", "special"},
                    new String[]{"", "", "Name", "Team", "Position", "Points", "Captain"},
                    gameweekTable, true,
                    new Class[]{Integer.class, Icon.class, String.class, String.class, String.class, Integer.class, String.class},
                    new int[][]{});
            storedData.put(gameweekInt-1, tableList);
        } else {
            tableList = storedData.get(gameweekInt);
        }

        initialiseTables(HistoryFileName.replace("{gameweek}", gameweekStr),
                new String[] {"keys", "values"},
                new String[] {"Gameweek", "Stats"},
                historyTable,false,
                new Class[] {String.class, String.class},
                new int[][] {});

        insertMyTeamData(labelArray, teamCards, tableList);
        return storedData;
    }

    public void customiseTable(JTable table) {
        tableHeaderRenderer headerRenderer = new tableHeaderRenderer();
        tableBodyRenderer bodyRenderer = new tableBodyRenderer();
        table.getTableHeader().setDefaultRenderer(headerRenderer);
        for (int i = 0; i < table.getColumnCount(); i++) {
            if (table.getColumnClass(i) != Icon.class) {
                table.getColumnModel().getColumn(i).setCellRenderer(bodyRenderer);
            }
        }
        table.setRowSelectionAllowed(false);
        table.setRowHeight(50);
        table.setGridColor(Color.lightGray);
    }

    public void initialiseMyTeam() {
        myTeamCards = createCards(new String[] {
                "myDEF3Card", "myDEF4Card", "myDEF5Card",
                "myMID2Card", "myMID3Card", "myMID4Card", "myMID5Card",
                "myFWD1Card", "myFWD2Card", "myFWD3Card"
        }, new JPanel[] {myDEFPanel, myMIDPanel, myFWDPanel});

        myStoredData = new LinkedHashMap<>();
        for (int i = 0; i < myGameweekArray.size(); i++) {
            myStoredData.put(i, null);
        }
    }

    public void initialisePredTeam() {
        predTeamCards = createCards(new String[] {
                "predDEF3Card", "predDEF4Card", "predDEF5Card",
                "predMID2Card", "predMID3Card", "predMID4Card", "predMID5Card",
                "predFWD1Card", "predFWD2Card", "predFWD3Card"
        }, new JPanel[] {predDEFPanel, predMIDPanel, predFWDPanel});

        predStoredData = new LinkedHashMap<>();
        for (int i = 0; i < predGameweekArray.size(); i++) {
            predStoredData.put(i, null);
        }
    }

    public void insertMyTeamData(JLabel[][][][] labelArrays, LinkedHashMap<JPanel, String[]> panels, ArrayList<LinkedHashMap<String, String>> tableList) {
        int[] formation = {1, 0, 0, 0};
        for (HashMap<String, String> player : tableList) {
            if (Integer.parseInt(player.get("position")) <= 11) {
                String position = player.get("position_name");
                switch (position) {
                    case "DEF":
                        formation[1] += 1;
                        break;
                    case "MID":
                        formation[2] += 1;
                        break;
                    case "FWD":
                        formation[3] += 1;
                        break;
                }
            }
        }

        setCard(panels, formation);

        for (HashMap<String, String> player : tableList) {
            int positionPos = 0;
            int formationPos = 0;
            int indexPos;
            int index = Integer.parseInt(player.get("position"));
            String position = player.get("position_name");
            String[] posNames = new String[] {"GKP", "DEF", "MID", "FWD"};
            if (index <= 11) {
                for (int i = 0; i < 4; i++) {
                    if (position.equals(posNames[i])) {
                        positionPos = i;
                    }
                }
                for (JLabel[][] formationArray : labelArrays[positionPos]) {
                    if (formation[positionPos] == formationArray.length) {
                        formationPos = Arrays.asList(labelArrays[positionPos]).indexOf(formationArray);
                    }
                }
                indexPos = index - 1;
                for (int i = 0; i < positionPos; i++) {
                    indexPos -= formation[i];
                }
            }
            else {
                positionPos = 4;
                indexPos = index - 12;
            }

            ImageIcon imageIcon = getPlayerImage(player.get("photo"), 55, 70);

            labelArrays[positionPos][formationPos][indexPos][0].setPreferredSize(new Dimension(85, 70));
            labelArrays[positionPos][formationPos][indexPos][0].setHorizontalAlignment(JLabel.RIGHT);
            labelArrays[positionPos][formationPos][indexPos][0].setIcon(imageIcon);

            labelArrays[positionPos][formationPos][indexPos][1].setPreferredSize(new Dimension(15, 70));
            labelArrays[positionPos][formationPos][indexPos][1].setHorizontalAlignment(JLabel.LEFT);
            labelArrays[positionPos][formationPos][indexPos][1].setVerticalAlignment(JLabel.TOP);
            labelArrays[positionPos][formationPos][indexPos][1].setText(player.get("special"));

            labelArrays[positionPos][formationPos][indexPos][2].setPreferredSize(new Dimension(100, 15));
            labelArrays[positionPos][formationPos][indexPos][2].setHorizontalAlignment(JLabel.CENTER);
            labelArrays[positionPos][formationPos][indexPos][2].setText(player.get("name"));

            labelArrays[positionPos][formationPos][indexPos][3].setPreferredSize(new Dimension(100, 15));
            labelArrays[positionPos][formationPos][indexPos][3].setHorizontalAlignment(JLabel.CENTER);
            labelArrays[positionPos][formationPos][indexPos][3].setText(player.get("points"));
        }
    }

    public void setCard(LinkedHashMap<JPanel, String[]> panels, int[] formation) {
        int i = 1;
        int[] amount = new int[] {3, 2, 1};
        for (JPanel panel : panels.keySet()) {
            CardLayout card = (CardLayout) panel.getLayout();
            card.show(panel, panels.get(panel)[formation[i]-amount[i-1]]);
            i += 1;
        }
    }

    public ImageIcon getPlayerImage(String path, int width, int height) {
        //https://stackoverflow.com/questions/32045075/how-to-display-my-image-from-a-url-into-my-jlabel-jframe
        try {
            URL url = new URL(AppConstants.urls.PLAYER_IMAGE_URL + path.replace(".jpg", ".png"));
            Image image = ImageIO.read(url);
            //https://stackoverflow.com/questions/6714045/how-to-resize-jlabel-imageicon
            Image newImage = image.getScaledInstance(width, height,  java.awt.Image.SCALE_SMOOTH);
            return new ImageIcon(newImage);  // transform it back
        }
        catch (IOException ignored) {
        }
        return null;
    }

    public LinkedHashMap<JPanel, String[]> createCards(String[] cardNames, JPanel[] panelNames) {
        LinkedHashMap<JPanel, String[]> cards = new LinkedHashMap<>();

        int cardCounter = 0;
        int panelCounter = 0;
        for (int amount : new int[] {3, 4, 3}) {
            String[] cardArray = new String[amount];
            for (int i = 0; i < amount; i++) {
                cardArray[i] = cardNames[cardCounter];
                cardCounter +=1;
            }
            cards.put(panelNames[panelCounter], cardArray);
            panelCounter += 1;
        }
        return cards;
    }
}