class Trie {

    static class Node {
        boolean isEnd;
        Node[] children = new Node[2];

        public Node() {
            this.isEnd = false;
            for (int i = 0; i < children.length; i++) {
                children[i] = null;
            }
        }
    }

    static Node root = new Node();

    public static void insert(Integer[] key) {
        Node proxy = root;

        for (int i = 0; i < key.length; i++) {
            if (proxy.children[key[i]] == null) {
                proxy.children[key[i]] = new Node();
            }
            proxy = proxy.children[key[i]];
        }

        proxy.isEnd = true;
    }

    public static boolean search(Integer[] key) {
        Node proxy = root;

        for (int i = 0; i < key.length; i++) {
            if (proxy.children[key[i]] == null) {
                return false;
            }
            proxy = proxy.children[key[i]];
        }

        return proxy.isEnd == true;
    }

}

public class Solution {
    static Trie.Node findUniqueRows(Integer[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            if (Trie.search(matrix[i]) == false) {
                Trie.insert(matrix[i]);
            }
        }

        return Trie.root;
    }

    public static void main(String[] args) {
        Integer[][] matrix = { 
            { 0, 1, 0, 0, 1 }, 
            { 1, 0, 1, 1, 0 }, 
            { 0, 1, 0, 0, 1 }, 
            { 1, 1, 1, 0, 0 } 
        };

        Trie.Node root = findUniqueRows(matrix);
    }
}