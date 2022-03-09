class BrowserHistory {
public:
    string browser[105] = {};
    int index = 0;
    int end = 0;
    BrowserHistory(string homepage) {
        browser[index] = homepage;
    }
    
    void visit(string url) {
        browser[++index] = url;
        end = index;
    }
    
    string back(int steps) {
        index = max(index - steps, 0);
        return browser[index];
    }
    
    string forward(int steps) {
        index = min(index + steps, end);
        return browser[index];
    }
};

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory* obj = new BrowserHistory(homepage);
 * obj->visit(url);
 * string param_2 = obj->back(steps);
 * string param_3 = obj->forward(steps);
 */