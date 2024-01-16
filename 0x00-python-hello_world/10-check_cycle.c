#include "lists.h"
/**
 * check_cycle - checks for a cycle
 * @list: list to be checked
 * Return: 1 or 0
 */
int check_cycle(listint_t *list)
{
	listint_t *li1 = list;
	listint_t *li2 = list;

	if (!list)
		return (0);
	while (li1 && li2 && li2->next)
	{
		li1 = li1->next;
		li2 = li2->next->next;

		if (li1 == li2)
			return (1);
	}
	return (0);
}
