#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/wait.h>
main()
{
  pid_t pid;
  int rv;
  switch(pid=fork()) {
  case -1:
        perror("fork"); /* произошла ошибка */
        exit(1); /*выход из родительского процесса*/
  case 0:
        printf(" CHILD: Это процесс-потомок!\n");
        printf(" CHILD: Мой PID -- %d\n", getpid());
        printf(" CHILD: PID моего родителя -- %d\n", getppid());
        printf(" CHILD: Введите мой код возврата (как можно меньше):");
        scanf("%d", &rv);
        printf(" CHILD: Выход!\n");
        printf(" child rv = %d\n", rv);
        exit(rv);
        /*родитель, и потомок используют переменную rv. Это не означает, что переменная
          разделена между процессами. Каждый процесс содержит собственные копии всех
          переменных.*/
  default:
        printf("PARENT: Это процесс-родитель!\n");
        printf("PARENT: Мой PID -- %d\n", getpid());
        printf("PARENT: PID моего потомка %d\n",pid);
        printf("PARENT: Я жду, пока потомок не вызовет exit()...\n");
        int status;
        wait(&status);
        printf("PARENT: Код возврата потомка:%d\n", WEXITSTATUS(rv));
        printf("PARENT: Выход!\n");
  }
}
