/*
	This file define functions o handle metadata of a in use script
*/
package wlua

import (
	"fmt"
	"github.com/yuin/gluamapper"
	lua "github.com/yuin/gopher-lua"
)

// Load metadata
func Meta(L *lua.LState) int {
	if err := gluamapper.Map(L.GetGlobal("Metadata").(*lua.LTable), &Metad); err != nil {
		panic(err)
	}
	return 1
}

func MetaShow() {
	println("## AUTHOR/S ##")
	MetaListAuthors()
	println("\n## CATEGORIES ##")
	MetaListCats()
	println("\n## INFO ##")
	MetaShowInfo()
}

func MetaListAuthors() {
	for i := range(Metad.AUTHOR) {
		fmt.Printf("%d) %s\n",i+1,Metad.AUTHOR[i])
	}
}

func MetaListCats() {
	for i := range(Metad.CATS) {
		fmt.Printf("%d) %s\n",i+1,Metad.CATS[i])
	}
}

func MetaShowInfo() {
	println(Metad.INFO)
}