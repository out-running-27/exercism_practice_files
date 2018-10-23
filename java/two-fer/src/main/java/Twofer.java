class Twofer {
    String twofer(String name) {
        String returnName;

        if (name != null) {
            returnName = name;
        } else {
            returnName = "you";
        }

        return String.format("One for %s, one for me.", returnName);
    }
}
