# Linear Search
# Time Complexity: O(n)
# Space Complexity: O(1)
def linear_search(array, target):
    for index in range(len(array)):
        if array[index] == target: return index
    return -1

# Binary Search
# Time Complexity: O(log2^2)
# Space Complexity: O(1) 
# NOTE: Sort in Ascending Order First ***
def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if array[mid] == target: return mid
        elif array[mid] < target: left = mid + 1
        else: right = mid - 1
    return -1

# Selection Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def selection_sort(array):
    for outer_index in range(len(array) - 1):
        index_min = outer_index
        for inner_index in range(outer_index+1, len(array)):
            if array[inner_index] < array[index_min]:
                index_min = inner_index
        if index_min != outer_index:
            temp = array[outer_index]
            array[outer_index] = array[index_min]
            array[index_min] = temp

# Bubble Sort
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def bubble_sort(array):
    size = len(array)
    count = 0
    for outer_index in range(size):
        count = 0
        for inner_index in range(size - outer_index - 1):
            if array[inner_index] > array[inner_index+1]:
                count += 1
                array[inner_index], array[inner_index + 1] = array[inner_index + 1], array[inner_index]
                print(array)
        if count == 0: 
            print("Already Sorted.")
            break


# Insertion Sort
# Time Complexity: Best Case O(n), Worst Case O(n^2)
def insertion_sort(array):
    for index in range(1, len(array)):
        prev_item = array[index]
        prev_index = index - 1
        while prev_index >= 0 and array[prev_index] > prev_item:
            array[prev_index + 1] = array[prev_index]
            prev_index -= 1
        array[prev_index + 1] = prev_item


data = [8, 2, 4, 1, 5] 
insertion_sort(data) 
print(data)

# ================================== Stack Implementaion in C =========================
# Stack Data structure Implementaion
# #include <stdio.h>
# #define MAX_NUMBERS 100
# typedef struct
# {
#     int top;
#     int data[MAX_NUMBERS];
# } Stack;

# void push(Stack *s, int value)
# {
#     if(s->top < MAX_NUMBERS)
#     {
#         s->data[s->top] = value;
#         s->top += 1;
#     }
#     else
#     {
#         printf("Reached the limit, Can't Store!");
#     }
# }
# int pop(Stack *s)
# {
#     if(s->top != 0)
#     {
#         s->top -= 1;
#         return s->data[s->top];
#     }
#     else
#     {
#         printf("There's no data in the array.At First push!");
#         return -1;
#     }
# }
# int main()
# {
# 	Stack s1;
# 	s1.top = 0;
	
# 	push(&s1, 2);
# 	push(&s1, 3);
# 	push(&s1, 5);
# 	int output1 = pop(&s1);
# 	int output2 = pop(&s1);
# 	int output3 = pop(&s1);
# 	printf("output 1: %d\n", output1);
# 	printf("output 2: %d\n", output2);
# 	printf("output 3: %d", output3);
	
	
# 	return 0;
# }
# ==================== Balanced Check ([{}]) ====================================

#include <stdio.h>
#include <string.h>
# int is_balanced(char array[])
# {
# 	int len, top, i;
# 	char last_item;
# 	len = strlen(array);
# 	char stack[len];
# 	top = 0;
# 	i = 0;
# 	for(; i<len; i++)
# 	{
# 		if(array[i] == '(' || array[i] == '[' || array[i] == '{')
# 		{
# 			stack[top] = array[i];
# 			top++;
# 		}
# 		else if(array[i] == ')' || array[i] == ']' || array[i] == '}')
# 		{
# 			if(top == 0)
# 			{
# 				return 0;
# 			}
# 			top--;
# 			last_item = stack[top];
# 			if (
# 			    (last_item == '(' && array[i] != ')') ||
# 			    (last_item == '{' && array[i] != '}') ||
# 			    (last_item == '[' && array[i] != ']')
# 			)
# 			{
# 				return 0;
# 			}
# 		}
# 	}
# 	if(top == 0)
# 	{
# 		return 1;
# 	} else return 0;
# }
# ======================== Undo-Redo using 2 Stacks ===========================
# Logic:
#     Action = Push to Undo, Clear Redo
#     Undo = Pop From Undo, Push to Redo
#     Redo = Popr From Redo, Push to Undo
#     New Action = Push to Undo, Clear Redo
#define MAX 100
# typedef struct
# {
#     int top;
#     char data[MAX];
# } StackUndo;
# typedef struct
# {
#     int top;
#     char data[MAX];
# } StackRedo;

# int Actions(StackUndo *undo, StackRedo *redo, char value)
# {
#     if(undo->top < MAX)
#     {
#         undo->data[undo->top] = value;
#         undo->top++;
#         redo->top = 0;
#         return 1;
#     }
#     return -1;
# }
# int Undo(StackUndo *undo, StackRedo *redo)
# {
#     if(undo->top != 0)
#     {
#         undo->top--;
#         char value = undo->data[undo->top];
#         redo->data[redo->top] = value;
#         redo->top++;
#         return value;
#     }
#     return -1;
# }
# int Redo(StackUndo *undo, StackRedo *redo)
# {
#     if(redo->top != 0)
#     {
#         redo->top--;
#         char value = redo->data[redo->top];
#         undo->data[undo->top] = value;
#         undo->top++;
#         return value;
#     }
#     return -1;
# }
# ===========================Queue Implementaion============================
# Queue Implementaion
#include <stdio.h>
#define SIZE 3
# typedef struct
# {
#     int data[SIZE + 1];
#     int head, tail;
# } Queue;
# int enqueue(Queue *q, int item)
# {
#     if((q->tail + 1) % (SIZE + 1) == q->head)
#     {
#         printf("Queue is full!\n");
#         return -1;
#     }
#     q->data[q->tail] = item;
#     q->tail = (q->tail + 1) % (SIZE + 1);
#     return 1;
# }
# int dequeue(Queue *q)
# {
#     int item;
#     if(q->head == q->tail)
#     {
#         printf("Queue is Empty!\n");
#         return -1;
#     }
#     item = q->data[q->head];
#     q->head = (q->head + 1) % (SIZE + 1);
#     return item;
# }


# int main()
# {
#     Queue q1 = {0};
#     enqueue(&q1, 2);
#     enqueue(&q1, 3);
#     enqueue(&q1, 5);
#     enqueue(&q1, 7);
#     printf("Value: 1: %d\n", dequeue(&q1));
#     printf("Value: 2: %d\n", dequeue(&q1));
#     printf("Value: 3: %d\n", dequeue(&q1));
#     printf("Value: 4: %d", dequeue(&q1));
#     return 0;
# }
# ============================== Singly Linked list Implementation ==============================
# // Singly Linked List Implementation
#include <stdio.h>
#include <stdlib.h>
# typedef struct node Node;
# struct node
# {
#   int data;
#   Node *next;
# };
# Node *create_node(Node *head, int data)
# {
#     Node *newNode = (Node *) malloc(sizeof(Node));
#     if(newNode == NULL)
#     {
#         printf("Something is wrong!");
#         exit(1);
#     }
#     newNode->data = data;
#     newNode->next = head;
#     return newNode;
# }
# Node *prepend(Node *head, int data)
# {
#     Node *newNode = create_node(head, data);
#     return newNode;
# }
# Node *append(Node *head, int data)
# {
#     Node *newNode = create_node(NULL, data);
#     Node *current_node = head;
#     if(head == NULL) return newNode;
#     while(current_node->next != NULL)
#     {
#         current_node = current_node->next;
#     }
#     current_node->next = newNode;
#     return head;
# }
# Node *remove_node(Node *head, Node *node)
# {
#     if(head == node)
#     {
#         head = node->next;
#         free(node);
#         return head;
#     }
#     Node *current_node = head;
#     while(current_node != NULL)
#     {
#         if(current_node->next == node)
#         {
#             current_node->next = node->next;
#             free(node);
#             return head;
#         }
#         current_node = current_node->next;
#     }
#     return head;
# }
# int count(Node *head)
# {
#     Node *current_node = head;
#     int count = 0;
#     while(current_node != NULL)
#     {
#         count++;
#         current_node = current_node->next;
#     }
#     if(count > 0) return count;
#     return -1;
# }
# void insert(Node* node, int data)
# {
#     Node *new_node = create_node(node->next, data);
#     node->next = new_node;
# }
# Node *search(Node *head, int data)
# {
#     Node *current_node = head;
#     while(current_node != NULL)
#     {
#         if(current_node->data == data)
#         {
#             return current_node;
#         }
#         current_node = current_node->next;
#     }
#     return NULL;
# }
# void print_linked_list(Node *head)
# {
#     Node *current_node = head;
#     while(current_node != NULL)
#     {
#         printf("%d\n", current_node->data);
#         current_node = current_node->next;
#     }
# }
# int main()
# {
# NOTE: append() always return the head that passed
# NOTE: headNode->next = newNode

#     Node *head, *n1;
#     head = create_node(NULL, 2);
#     head = prepend(head, 1);
#     head = append(head, 4);
#     n1 = search(head, 2);
#     insert(n1, 3);
#     head = remove_node(head, n1);
#     head = append(head, 5);
#     head = append(head, 6);
#     print_linked_list(head);
#     if(count(head) > 0) printf("Count: %d\n", count(head));
#     return 0;
# }

