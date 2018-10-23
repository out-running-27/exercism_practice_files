class ReverseString {

    String reverse(String inputString) {
        StringBuilder gnirtStupni = new StringBuilder(inputString.length());

        for (int i = inputString.length() - 1; i >= 0; i--) {
            gnirtStupni.append(inputString.charAt(i));
        }

        return gnirtStupni.toString();
    }
}