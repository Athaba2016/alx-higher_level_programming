#ifndef LISTS_H
#define LISTS_H

<<<<<<< HEAD
#include <stdlib.h>
=======
#include <stdio.h>
>>>>>>> e39111d0307c8c255d77e0258545936347243d0a

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
<<<<<<< HEAD
 *
 */
typedef struct listint_s
{
        int n;
        struct listint_s *next;
=======
 */
typedef struct listint_s
{
	int n;
	struct listint_s *next;
>>>>>>> e39111d0307c8c255d77e0258545936347243d0a
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);
<<<<<<< HEAD
listint_t *insert_node(listint_t **head, int number);

#endif
=======

listint_t *insert_node(listint_t **head, int number);

#endif /* LISTS_H */
>>>>>>> e39111d0307c8c255d77e0258545936347243d0a
