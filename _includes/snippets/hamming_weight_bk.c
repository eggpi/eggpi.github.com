#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    int fd;
    register int i;
    unsigned long rd, sum = 0;
    unsigned char buf[BUFSIZ];

    fd = open(argv[1], O_RDONLY);
    while ((rd = read(fd, &buf, BUFSIZ)) > 0) {
        for (i = 0; i < rd; i++) {
            for (; buf[i]; sum++)
                buf[i] &= (buf[i]-1);
        }
    }

    close(fd);
    printf("total bits set: %lu\n", sum);
    return 0;
}
