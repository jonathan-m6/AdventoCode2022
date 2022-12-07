package main

import (
	"io/ioutil"
	"log"
	"strings"
)

func main() {
	datosComoBytes, err := ioutil.ReadFile("recurso.txt")
	if err != nil {
		log.Fatal(err)
	}
	datos := strings.Split(string(datosComoBytes), "\r\n")
	//dia1(datos)
	dia2(datos)
}
func dia1(datos []string) {
	suma := 0
	for i := 0; i < len(datos); i++ {
		duendeJugada := jugada(strings.Split(datos[i], " ")[0])
		miJugada := jugada(strings.Split(datos[i], " ")[1])
		suma += conteoPuntos(duendeJugada, miJugada)
	}
	println(suma)
}

func dia2(datos []string) {
	suma := 0
	for i := 0; i < len(datos); i++ {
		duendeJugada := jugada(strings.Split(datos[i], " ")[0])
		miJugada := getMiJugada(duendeJugada, strings.Split(datos[i], " ")[1])
		suma += conteoPuntos(duendeJugada, miJugada)
	}
	println(suma)
}
func getMiJugada(duendeJugada string, codigo string) string {
	miJugada := ""
	switch codigo {
	case "X":
		switch duendeJugada {
		case "piedra":
			miJugada = "tijeras"
		case "papel":
			miJugada = "piedra"
		case "tijeras":
			miJugada = "papel"
		}
	case "Y":
		miJugada = duendeJugada
	case "Z":
		switch duendeJugada {
		case "piedra":
			miJugada = "papel"
		case "papel":
			miJugada = "tijeras"
		case "tijeras":
			miJugada = "piedra"
		}
	}
	return miJugada
}

func conteoPuntos(duendeJugada string, miJugada string) int {
	puntos := 0
	if duendeJugada == miJugada {
		puntos = puntos + 3 + getPuntos(miJugada)
	} else {
		if (miJugada == "piedra" && duendeJugada == "tijeras") || (miJugada == "tijeras" && duendeJugada == "papel") || (miJugada == "papel" && duendeJugada == "piedra") {
			puntos = puntos + 6 + getPuntos(miJugada)
		} else {
			puntos = puntos + getPuntos(miJugada)
		}
	}
	return puntos
}
func getPuntos(jugada string) int {
	puntos := 0
	switch jugada {
	case "piedra":
		puntos = 1
	case "papel":
		puntos = 2
	case "tijeras":
		puntos = 3
	}
	return puntos
}
func jugada(codigo string) string {
	jugadaRealizada := ""
	switch codigo {
	case "A":
		jugadaRealizada = "piedra"
	case "B":
		jugadaRealizada = "papel"
	case "C":
		jugadaRealizada = "tijeras"
	case "X":
		jugadaRealizada = "piedra"
	case "Y":
		jugadaRealizada = "papel"
	case "Z":
		jugadaRealizada = "tijeras"
	}
	return jugadaRealizada
}
