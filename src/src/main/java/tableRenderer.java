import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import java.awt.*;

class tableHeaderRenderer extends DefaultTableCellRenderer {
    public tableHeaderRenderer() {
        super.setOpaque(true);
    }

    @Override
    public Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int column) {
        super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
        setFont(new Font("Quicksand", Font.BOLD, 13));
        setHorizontalAlignment(CENTER);
        setBorder(noFocusBorder);
        return this;
    }
}

class tableBodyRenderer extends DefaultTableCellRenderer {
    public tableBodyRenderer() {
        super.setOpaque(true);
    }

    @Override
    public Component getTableCellRendererComponent(JTable table, Object value, boolean isSelected, boolean hasFocus, int row, int column) {
        super.getTableCellRendererComponent(table, value, isSelected, hasFocus, row, column);
        setFont(new Font("Quicksand", Font.PLAIN, 15));
        setHorizontalAlignment(CENTER);
        setBorder(noFocusBorder);
        return this;
    }
}