from stackoverflow import jobs

app = jobs.create_app()

if __name__ == "__main__":
  app.run()