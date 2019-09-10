from orator.migrations import Migration


class CreateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.create('users') as table:
            table.string('id').unique()
            table.string('name', 100)
            table.text('password')
            table.string('username', 50)
            table.timestamps()
            table.primary('id')
            table.unique('username')

    def down(self):
        """
        Revert the migrations.
        """
        self.schema.drop('users')
