import { fireEvent, render, screen } from "@testing-library/react";
import { describe, expect, test } from "vitest";
import { Concat } from "../pages/Concat";


describe('Testing Contac Component', () => {
    test('verificar render title h1', () => {
        render(<Concat />)          
        const title = screen.getByText(/Envianos tu consulta/i)
        expect(title).toBeDefined()
    })
    test('should render first input', () => {
      render(<Concat />)
      const email = screen.getByRole('email')
      expect(email).toBeDefined()
      })
      
      // Iteractuamos ocn le imput, validamos lo que esta escrito se encuentre ahi
      test('Sohould change scond input', () => {
        render(<Concat />)
        const mensaje =  screen.getByTestId('consulta')
        fireEvent.change(mensaje, {target: {value: 'Hacen recetas de dieta queto'}})
        expect(mensaje.value).toBe('Hacen recetas de dieta queto')

        })
        test('Should fire click event', () => {
            const handleClick = vi.fn()
            render(<Concat onClick = {handleClick}/>)
            const btn = screen.getByText('Enviar')
            fireEvent.click(btn)
            //fireEvent.click(btn)
            expect(handleClick).toBeCalledTimes(1)
        })
})