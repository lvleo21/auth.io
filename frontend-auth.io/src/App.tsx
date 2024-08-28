import { useForm } from "react-hook-form"
import { Link } from "react-router-dom"
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import { Input } from "@/components/ui/input"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"

import { buttonVariants } from "@/components/ui/button"
import cn from "./lib/utils"





import { Button } from "@/components/ui/button"

function App() {
  const form = useForm();

  return (
    <>
      <div className="w-screen h-screen flex justify-center items-center">
        <Card className="shadow-lg">
          <CardHeader className="text-center">
            <CardTitle>Login</CardTitle>
            <CardDescription>
              Continue your onbording with Auth.io
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Form {...form}>
              <form className="space-y-6">
                <FormField
                  name="username"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Username</FormLabel>
                      <FormControl>
                        <Input placeholder="Insert your username..." {...field} />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />
                <FormField
                  name="password"
                  render={({ field }) => (
                    <FormItem>
                      <FormLabel>Password</FormLabel>
                      <FormControl>
                        <Input placeholder="Insert your password..." {...field} type="password" />
                      </FormControl>
                      <FormMessage />
                    </FormItem>
                  )}
                />
                <Button className="w-full" type="submit">Sign in</Button>
                <Link className={buttonVariants({ variant: "link", size: "sm" })} to="#">
                  Don't have a account? Register now
                </Link>
              </form>
            </Form>
          </CardContent>
        </Card>
      </div>
    </>
  )
}

export default App
