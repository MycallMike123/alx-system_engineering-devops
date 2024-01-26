#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"

/**
 * infinite_ - a function that runs forever and returns nothing
 * Return: 0 in the end
*/
int infinite_(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - the entry to a program that creats 5 zombie process
 * Return: 0 on sucess
*/
int main(void)
{
	int child_pid = 0;
	pid_t pid_t;

	while (child_pid < 5)
	{
		pid_t = fork();
		if (!pid_t)
			break;
		printf("Zombie process created, PID: %i\n", (int)pid_t);
		child_pid++;
	}

	if (pid_t != 0)
		infinite_();
	return (0);
}
