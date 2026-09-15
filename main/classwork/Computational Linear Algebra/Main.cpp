#include <iostream>

using namespace std;

struct Node {
    int data;
    Node* next;
};

class LinkedList {
    private:
    Node* head;

    public:
    LinkedList() {
        head = nullptr;
    }

    void insert(int value) {
        Node* newNode = new Node;
        newNode->data = value;
        newNode->next = head; 
        head = newNode; 
    }

    void printList() {
        Node *current = head;
        while(current != nullptr) {
            cout << current->data << " " << endl;
            current = current->next;
         } 
    }
};


int main() {
    LinkedList listMain;
    listMain.insert(10);
    listMain.insert(20);
    listMain.printList();
    return 0;
}