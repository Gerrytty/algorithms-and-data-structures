class OrderedStream {

    private int ptr = 1;
    private String[] stream;
    private int max = 0;
    int n = 0;

    public OrderedStream(int n) {
        stream = new String[n];
        this.n = n;
    }
    
    public List<String> insert(int idKey, String value) {

        List<String> arr = new ArrayList<>();

        stream[idKey-1] = value;

        int c = ptr-1;
        String curr = stream[c];
        while (c < n && curr != null) {
            curr = stream[c++];
            ptr = c;
            if (curr == null) {
                break;
            }
            arr.add(curr);
            
        }

        return arr;
    }
}

/**
 * Your OrderedStream object will be instantiated and called as such:
 * OrderedStream obj = new OrderedStream(n);
 * List<String> param_1 = obj.insert(idKey,value);
 */