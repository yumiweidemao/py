#include <iostream>

// function prototypes
int partition(int A[], int p, int r);
void quick_sort(int A[], int p, int r);

/* This program implements quick sort to sort an array in descending order. */
int main() {
    // test quick_sort function
    int array[9] = {6, 8, 4, 2, 5, 1, 9, 3, 7};
    int solution[9] = {9, 8, 7, 6, 5, 4, 3, 2, 1};
    std::cout << "Testing quick_sort: " << std::endl;
    quick_sort(array, 0, 8);
    bool success = true;
    for (int i = 0; i < 9; i++) {
        if (array[i] != solution[i]) {
            success = false;
        }
    }
    if (success) {
        std::cout << "quick_sort succeeded." << std::endl;
    } else {
        std::cout << "quick_sort failed." << std::endl;
        return 1;
    }
    return 0;
}

/*  
    @brief  returns an index q such that everything before A[q] is smaller than it, 
            everything after A[q] is larger than it.
    @params A: array of integers
            p: starting index
            r: ending index
    @retval q: an index
*/
int partition(int A[], int p, int r) {
    int reference = A[r];
    int i = p - 1;
    for (int j = p; j < r; j++) {
        if (A[j] >= reference) {
            // increment pointer
            i++;

            // exchange A[j] with A[i]
            int* temp = new int;
            *temp = A[j];
            A[j] = A[i];
            A[i] = *temp;
            delete temp;
        }
    }
    // exchange A[i+1] with A[r]
    int* temp = new int;
    *temp = A[i+1];
    A[i+1] = A[r];
    A[r] = *temp;
    delete temp;

    return (i+1);
}

/*
    @brief  sort an array in descending order.
    @params A: array of integers
            p: starting index
            r: ending index
    @retval none
 */
void quick_sort(int A[], int p, int r) {
    if (p < r) {
        int q = partition(A, p, r);
        quick_sort(A, p, q-1);
        quick_sort(A, q+1, r);
    }
}