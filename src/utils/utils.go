package utils

import (
	"os"
	"os/exec"
	"fmt"
)

func GetBash() {
	cmd := exec.Command("bash")
	cmd.Stdin = os.Stdin
	cmd.Stdout = os.Stdout
	cmd.Stderr = os.Stderr
	cmd.Run()
}

// Types of pretty printing
func PrintSuccs(s string) {
	fmt.Printf("[\u001B[1;32mOK\u001B[0;0m]- %s\n",s)
}
func PrintErr(s string) {
	fmt.Printf("[\u001B[1;31m!\u001B[0;0m]- %s\n",s)
}
func PrintAlert(s string) {
	fmt.Printf("[\u001B[1;31m!\u001B[0;0m]- %s\n",s)
}